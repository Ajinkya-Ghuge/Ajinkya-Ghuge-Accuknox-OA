from django.test import TestCase
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from signals_demo.models import TestModel
import threading
import time


class SignalSynchronousTestCase(TestCase):
    def test_signals_are_synchronous(self):
        execution_order = []
        
        @receiver(post_save, sender=TestModel)
        def sync_test_handler(sender, instance, **kwargs):
            execution_order.append('signal_start')
            time.sleep(0.1)
            execution_order.append('signal_end')
        
        execution_order.append('before_create')
        TestModel.objects.create(name="Sync Test")
        execution_order.append('after_create')
        
        expected_order = ['before_create', 'signal_start', 'signal_end', 'after_create']
        self.assertEqual(execution_order, expected_order)


class SignalThreadTestCase(TestCase):
    def test_signals_run_in_same_thread(self):
        caller_thread_id = threading.current_thread().ident
        signal_thread_id = None
        
        @receiver(post_save, sender=TestModel)
        def thread_test_handler(sender, instance, **kwargs):
            nonlocal signal_thread_id
            signal_thread_id = threading.current_thread().ident
        
        TestModel.objects.create(name="Thread Test")
        
        self.assertEqual(caller_thread_id, signal_thread_id)


class SignalTransactionTestCase(TestCase):
    def test_signals_run_in_same_transaction(self):
        signal_saw_object = False
        
        @receiver(post_save, sender=TestModel)
        def transaction_test_handler(sender, instance, **kwargs):
            nonlocal signal_saw_object
            signal_saw_object = TestModel.objects.filter(id=instance.id).exists()
        
        try:
            with transaction.atomic():
                obj = TestModel.objects.create(name="Transaction Test")
                raise Exception("Rollback")
        except:
            pass
        
        self.assertTrue(signal_saw_object)
        self.assertFalse(TestModel.objects.filter(name="Transaction Test").exists())
