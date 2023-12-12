from celery import shared_task
from django.core.mail import send_mail
from .models import Order
import time


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании
   заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order.\nYour order id is {}.'.format(order.first_name,
                                                                                                order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent


@shared_task
def simple_task():
    """
    Простая задача для проверки работы Celery.
    """
    print("Simple task started")
    # Добавим задержку на 5 секунд для имитации долгой работы
    time.sleep(5)
    print("Simple task completed")
    return "Task completed successfully"
