from django.test import TestCase
from .models import YourModel

class YourModelTests(TestCase):

    def test_model_creation(self):
        model_instance = YourModel.objects.create(field_name='value')
        self.assertEqual(model_instance.field_name, 'value')

    def test_model_str(self):
        model_instance = YourModel(field_name='value')
        self.assertEqual(str(model_instance), 'value')

    # Add more tests as needed for your application