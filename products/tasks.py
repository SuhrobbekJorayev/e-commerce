import requests
from celery import shared_task
from django.conf import settings


@shared_task
def send_telegram_notification(order_id, product_name, quantity, customer_username, phone_number):
    token = settings.TELEGRAM_BOT_TOKEN
    method = 'sendMessage'
    message_text = (f'New Order: {order_id}\n Product: {product_name}\n '
                    f'Quantity: {quantity}\n Client: {customer_username}\n Tel: {phone_number}')
    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': 5865572819, 'message': message_text}
    ).json()
