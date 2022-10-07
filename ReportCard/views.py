import io

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from ACL.mixins import PermissionMixin, VerifiedUserMixin
from config.settings import BASE_DIR
from utils.utils import render_to_pdf
from .filters import ReportCardFilters
from .forms import *
from .models import ReportCard


class ReportCardsListView(PermissionMixin, ListView):
    permissions = ['report_card_list']
    model = ReportCard
    context_object_name = 'report_cards'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'report_cards/admin/report_cards/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return ReportCardFilters(data=self.request.GET, queryset=queryset).qs


class ReportCardsCreateView(PermissionMixin, CreateView):
    permissions = ['report_card_create']
    template_name = "report_cards/admin/report_cards/form.html"
    model = ReportCard
    form_class = ReportCardForm
    success_url = reverse_lazy("report-card-list")


class ReportCardsUpdateView(PermissionMixin, UpdateView):
    permissions = ['report_card_edit']
    template_name = "report_cards/admin/report_cards/form.html"
    model = ReportCard
    form_class = ReportCardForm
    success_url = reverse_lazy("report-card-list")


class ReportCardsDeleteView(PermissionMixin, DeleteView):
    permissions = ['report_card_delete']
    model = ReportCard
    template_name = 'report_cards/admin/report_cards/list.html'
    success_url = reverse_lazy("report-card-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


# PDF
class ReportCardsPDFView(VerifiedUserMixin, DetailView):
    model = ReportCard
    template_name = 'report_cards/pdf_files/term.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['base_dir'] = BASE_DIR
        return context

    def get_template_names(self):
        if self.object.type == 'ttc':
            self.template_name = 'report_cards/pdf_files/ttc.html'
        elif self.object.type == 'mock':
            self.template_name = 'report_cards/pdf_files/mock.html'

        return self.template_name

    # def render_to_response(self, context, **kwargs):
    #     if self.object.type == 'ttc':
    #         self.template_name = 'report_cards/pdf_files/ttc.html'
    #     elif self.object.type == 'mock':
    #         self.template_name = 'report_cards/pdf_files/mock.html'
    #
    #     pdf = render_to_pdf(self.template_name, context)
    #
    #     # response = FileResponse(pdf, content_type='application/force-download')
    #     # response['Content-Disposition'] = 'inline; filename="report-card.pdf"'
    #     # return response
    #
    #     return HttpResponse(pdf, content_type='application/pdf')
