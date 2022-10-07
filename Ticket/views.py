# from Subscription.models import Type
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
# from Subscription.models import Type
from User.forms import UserSimpleForm
from ACL.mixins import VerifiedUserMixin, AnonymousUserMixin, SuperUserRequiredMixin, PermissionMixin
# from .filters import TicketFilters
from .filters import TicketFilters
from .forms import *
from .mixins import FilterTicketsQuerysetMixin
from .models import Ticket, TicketCategory
from django.conf import settings
from django.contrib import messages


class TicketCategoryListView(SuperUserRequiredMixin, ListView):
    model = TicketCategory
    context_object_name = 'sliders'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'tickets/admin/categories/list.html'
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return TicketCategoryFilters(data=self.request.GET, queryset=queryset).qs


class TicketCategoryCreateView(SuperUserRequiredMixin, CreateView):
    template_name = "tickets/admin/categories/form.html"
    model = TicketCategory
    form_class = TicketCategoryForm
    success_url = reverse_lazy("ticket-categories-list")


class TicketCategoryUpdateView(SuperUserRequiredMixin, UpdateView):
    template_name = "tickets/admin/categories/form.html"
    model = TicketCategory
    form_class = TicketCategoryForm
    success_url = reverse_lazy("ticket-categories-list")


class TicketCategoryDeleteView(SuperUserRequiredMixin, DeleteView):
    model = TicketCategory
    template_name = 'tickets/admin/categories/list.html'
    success_url = reverse_lazy("ticket-categories-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Ticket """


class TicketsListView(PermissionMixin, FilterTicketsQuerysetMixin, ListView):
    permissions = ['ticket_list']
    model = Ticket
    context_object_name = 'sliders'
    paginate_by = settings.PAGINATION_NUMBER
    ordering = ['-created_at']
    template_name = 'tickets/admin/tickets/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['category_filter_items'] = [{"name": i.title, "id": i.id} for i in TicketCategory.objects.all()]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return TicketFilters(data=self.request.GET, queryset=queryset).qs


class TicketsCreateView(PermissionMixin, CreateView):
    permissions = ['ticket_create']
    template_name = "tickets/admin/tickets/form.html"
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy("tickets-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class TicketsUpdateView(PermissionMixin, FilterTicketsQuerysetMixin, UpdateView):
    permissions = ['ticket_edit']
    template_name = "tickets/admin/tickets/form.html"
    model = Ticket
    form_class = TicketForm
    success_url = reverse_lazy("tickets-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class TicketsDeleteView(PermissionMixin, FilterTicketsQuerysetMixin, DeleteView):
    permissions = ['ticket_delete']
    model = Ticket
    template_name = 'tickets/admin/tickets/list.html'
    success_url = reverse_lazy("tickets-list")

    def dispatch(self, *args, **kwargs):
        resp = super().dispatch(*args, **kwargs)
        messages.success(self.request, 'آیتم مورد نظر با موفقیت حدف شد.')
        return resp


""" Ticket Answers """


class TicketAnswersListView(PermissionMixin, FilterTicketsQuerysetMixin, DetailView):
    permissions = ['ticket_answer_list', 'ticket_answer_create']
    model = Ticket
    template_name = 'tickets/admin/answers/list.html'

    @property
    def ticket(self):
        return get_object_or_404(Ticket, id=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({"form": TicketAnswerForm()})
        ctx.update({"object_list": self.object.answers.all()})
        return ctx


class TicketAnswersCreateView(PermissionMixin, CreateView):
    permissions = ['ticket_answer_create']
    model = Ticket
    form_class = TicketAnswerForm
    template_name = 'tickets/admin/answers/list.html'

    @property
    def ticket(self):
        return get_object_or_404(Ticket, id=self.kwargs.get("pk"))

    def get_success_url(self):
        return reverse_lazy('tickets-answers-list', kwargs={'pk': self.ticket.id})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'ticket': self.ticket})
        kwargs.update({'request': self.request})
        return kwargs
