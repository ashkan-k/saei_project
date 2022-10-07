import jdatetime
from django import template

register = template.Library()


@register.simple_tag
def class_users_js_list(value):
    users_data = list(value.users.values('id', 'user', 'status'))
    return users_data


@register.filter
def check_class_users_exists(class_item, user):
    user_class = user.classes.filter(class_item_id=class_item.id, status='active').first()
    if user_class:
        return True

    class_user_installment = user.installments.filter(class_item=class_item).first()

    if not class_user_installment:
        return False

    # Check installment is completed items or payment date not reach
    if class_user_installment.is_complete:
        return True

    if class_user_installment.payment_date and class_user_installment.payment_date > jdatetime.datetime.now().date():
        return True


@register.simple_tag
def get_current_class_user(class_item, user):
    user_class = user.classes.filter(class_item_id=class_item.id, status='active').first()
    return user_class
