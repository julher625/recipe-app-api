from django.test import TestCase

from app.calc import add, substract

class CalcTests(TestCase):
    
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3,2),5)

    def test_substract_numbers(self):
        """Test that two numbers are substracted together"""
        self.assertEqual(substract(11,6),5)