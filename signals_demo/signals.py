from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TestModel
import time
import threading


@receiver(post_save, sender=TestModel)
def test_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal received for: {instance.name}")
    time.sleep(2)
    print(f"Signal handler finished for: {instance.name}")
