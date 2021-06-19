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
