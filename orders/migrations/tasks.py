from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send and e-mail notification when an order is 
    successfully created.
    """
