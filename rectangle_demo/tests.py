from django.test import TestCase
from rectangle_demo.rectangle import Rectangle


class RectangleTestCase(TestCase):
    def test_rectangle_initialization(self):
        rect = Rectangle(length=15, width=10)
        self.assertEqual(rect.length, 15)
        self.assertEqual(rect.width, 10)
    
    def test_rectangle_iteration(self):
        rect = Rectangle(length=20, width=8)
        items = list(rect)
        
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0], {'length': 20})
        self.assertEqual(items[1], {'width': 8})
    
    def test_rectangle_iteration_order(self):
        rect = Rectangle(length=100, width=50)
        iterator = iter(rect)
        
        first = next(iterator)
        self.assertIn('length', first)
        self.assertEqual(first['length'], 100)
        
        second = next(iterator)
        self.assertIn('width', second)
        self.assertEqual(second['width'], 50)
