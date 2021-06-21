from datetime import datetime
from django.test import TestCase

from app_ts.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Victor Hugo',
            cpf='12345678901',
            email='victor-hugo-py@outlook.com',
            phone='81-998832982',
            lecture_theme='Pythonico'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr"""
        self.assertIsInstance(
            self.obj.created_at,
            datetime
        )

    def test_str(self):
        self.assertEqual(
            'Victor Hugo',
            str(self.obj)
        )
