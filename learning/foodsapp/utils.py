from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import OrderItem


def send_email_view(email, user, order, address):
    subject = "Your order & payment is successful ✅"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

   
    order_items = OrderItem.objects.filter(order=order)

    html_message = render_to_string(
        "emails/bill_invoice_template.html",
        {
            "user": user,
            "order": order,
            "order_items": order_items,
            "address": address,
        },
    )

    plain_message = strip_tags(html_message)

    send_mail(
        subject=subject,
        message=plain_message,
        from_email=from_email,
        recipient_list=recipient_list,
        html_message=html_message,
        fail_silently=False,
    )


