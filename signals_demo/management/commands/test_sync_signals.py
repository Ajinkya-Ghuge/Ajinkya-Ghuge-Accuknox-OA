from django.core.management.base import BaseCommand
from signals_demo.models import TestModel
import time


class Command(BaseCommand):
    help = 'Demonstrates that Django signals execute synchronously'

    def handle(self, *args, **kwargs):
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Question 1: Are Django signals synchronous?")
        self.stdout.write("="*60 + "\n")
        
        start_time = time.time()
        self.stdout.write(f"[{time.time() - start_time:.2f}s] Starting to create object...")
        
        obj = TestModel.objects.create(name="Test Object", description="Testing sync behavior")
        
        self.stdout.write(f"[{time.time() - start_time:.2f}s] Object creation completed")
        self.stdout.write(f"[{time.time() - start_time:.2f}s] Back to main code\n")
        
        self.stdout.write("="*60)
        self.stdout.write("CONCLUSION:")
        self.stdout.write("The signal handler added a 2-second delay.")
        self.stdout.write("If signals were asynchronous, object creation would")
        self.stdout.write("complete immediately (around 0.00s).")
        self.stdout.write("Since it took ~2 seconds, signals are SYNCHRONOUS.")
        self.stdout.write("="*60)
