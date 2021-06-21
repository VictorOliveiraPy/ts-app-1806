from django.test import TestCase

from app_ts.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Victor Hugo',
            cpf='12345678901',
            email='victor-hugopy@outlook.com',
            phone='81-998834932',
            lecture_theme='pythonico'
        )
        self.resp = self.client.get(
            r('subscription:subscription-detail',
            self.obj.pk)
        )

    def test_get(self):
        self.assertEqual(
            200,
            self.resp.status_code
        )

    def test_template(self):
        self.assertTemplateUsed(
            self.resp,
            'subscription/detail_subscription.html'
        )

    def test_html(self):
        contents = (
            self.obj.name,
            self.obj.cpf,
            self.obj.email,
            self.obj.phone,
            self.obj.lecture_theme
        )

        with self.subTest():
            for expected in contents:
                self.assertContains(
                    self.resp,
                    expected
                )


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(
            r('subscription:subscription-detail',
              0)
        )
        self.assertEqual(
            404,
            resp.status_code
        )
