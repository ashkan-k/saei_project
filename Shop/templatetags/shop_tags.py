from django import template

register = template.Library()


@register.filter
def check_user_bought_product(user, product):
    return user.products.filter(product=product, status=True).exists()
