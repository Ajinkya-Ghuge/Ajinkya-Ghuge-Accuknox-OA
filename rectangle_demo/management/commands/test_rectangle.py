from django.core.management.base import BaseCommand
from rectangle_demo.rectangle import Rectangle


class Command(BaseCommand):
    help = 'Demonstrates the Rectangle class with iteration support'

    def handle(self, *args, **kwargs):
        self.stdout.write("\n" + "="*60)
        self.stdout.write("Custom Classes in Python: Rectangle Class")
        self.stdout.write("="*60 + "\n")
        
        self.stdout.write("Creating a Rectangle with length=10 and width=5\n")
        rect = Rectangle(length=10, width=5)
        
        self.stdout.write("Iterating over the Rectangle instance:\n")
        for item in rect:
            self.stdout.write(str(item))
        
        self.stdout.write("\n" + "="*60)
        self.stdout.write("VERIFICATION:")
        self.stdout.write("1. Rectangle initialized with length and width")
        self.stdout.write("2. Rectangle instance is iterable")
        self.stdout.write("3. First iteration yields {'length': value}")
        self.stdout.write("4. Second iteration yields {'width': value}")
        self.stdout.write("="*60)
