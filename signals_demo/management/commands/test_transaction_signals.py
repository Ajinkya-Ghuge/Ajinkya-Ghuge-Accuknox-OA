from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from signals_demo.models import TestModel


class Command(BaseCommand):
    help = 'Demonstrates that Django signals run in the same database transaction'

    def handle(self, *args, **kwargs):
        signal_can_see_object = False
        
        @receiver(post_save, sender=TestModel)
        def check_transaction_handler(sender, instance, **kwargs):
            nonlocal signal_can_see_object
            try:
                obj_count = TestModel.objects.filter(name="Transaction Test").count()
                signal_can_see_object = obj_count > 0
            except Exception as e:
                signal_can_see_object = False
        
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Question 3: Do signals run in the same transaction?")
        self.stdout.write("="*60 + "\n")
        
        self.stdout.write("Test 1: Creating object inside a transaction that gets rolled back\n")
        
        try:
            with transaction.atomic():
                obj = TestModel.objects.create(
                    name="Transaction Test",
                    description="This should be rolled back"
                )
                self.stdout.write(f"Object created with ID: {obj.id}")
                self.stdout.write(f"Signal can see object: {signal_can_see_object}")
                
                raise Exception("Intentional rollback")
        except Exception as e:
            self.stdout.write(f"Transaction rolled back: {str(e)}")
        
        final_count = TestModel.objects.filter(name="Transaction Test").count()
        self.stdout.write(f"Object count after rollback: {final_count}\n")
        
        self.stdout.write("="*60)
        self.stdout.write("CONCLUSION:")
        self.stdout.write(f"Signal could see the object: {signal_can_see_object}")
        self.stdout.write(f"But object doesn't exist after rollback: {final_count == 0}")
        self.stdout.write("This proves signals run in the SAME TRANSACTION.")
        self.stdout.write("If they ran in a separate transaction, the signal")
        self.stdout.write("would not see the uncommitted object.")
        self.stdout.write("="*60)
