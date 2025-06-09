from django.db.models.signals import post_save
from django.db.models.signals import post_delete
from django.dispatch import receiver
from orders.models import Order
from utilis.telegram import send_telegram_message

@receiver(post_save, sender=Order)
def notify_new_order(sender, instance, created, **kwargs):
    if created:
        total_price = instance.calculate_total_price()
        message = (
            f"📦 Новый заказ #{instance.id} от {instance.client_name}!\n"
            f"Телефон: {instance.client_phone}\n"
            f"Адрес: {instance.client_address}\n"
            f"Сумма: {total_price} сом."
        )
        send_telegram_message(message)



@receiver(post_delete, sender=Order)
def notify_order_deleted(sender, instance, **kwargs):
    message = f"❌ Заказ #{instance.id} от {instance.client_name} был удалён."
    send_telegram_message(message)
