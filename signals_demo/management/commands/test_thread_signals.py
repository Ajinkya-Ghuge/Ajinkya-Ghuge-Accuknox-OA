from django.core.management.base import BaseCommand
from django.db.models.signals import post_save
from django.dispatch import receiver
from signals_demo.models import TestModel
import threading


class Command(BaseCommand):
    help = 'Demonstrates that Django signals run in the same thread as the caller'

    def handle(self, *args, **kwargs):
        caller_thread_id = None
        signal_thread_id = None
        
        @receiver(post_save, sender=TestModel)
        def check_thread_handler(sender, instance, **kwargs):
            nonlocal signal_thread_id
            signal_thread_id = threading.current_thread().ident
        
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Question 2: Do signals run in the same thread?")
        self.stdout.write("="*60 + "\n")
        
        caller_thread_id = threading.current_thread().ident
        self.stdout.write(f"Caller thread ID: {caller_thread_id}")
        
        obj = TestModel.objects.create(name="Thread Test", description="Testing thread behavior")
        
        self.stdout.write(f"Signal thread ID: {signal_thread_id}\n")
        
        self.stdout.write("="*60)
        self.stdout.write("CONCLUSION:")
        if caller_thread_id == signal_thread_id:
            self.stdout.write("Both IDs are IDENTICAL.")
            self.stdout.write("Django signals run in the SAME THREAD as the caller.")
        else:
            self.stdout.write("IDs are different.")
            self.stdout.write("Signals run in a DIFFERENT THREAD.")
        self.stdout.write("="*60)
