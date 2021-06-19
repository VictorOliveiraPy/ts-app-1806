from django.core import mail
from django.test import TestCase
from app_ts.subscriptions.forms import SubscriptionForm
from app_ts.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionsCreateGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscription:subscription'))

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_added.html"""
        self.assertTemplateUsed(self.resp,
                                'subscription/subscription_added.html')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
 
    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscriptionCreatePost(TestCase):
    def setUp(self):
        data = dict(name='Victor', cpf='12345678901',
                    email='testing@gmail.com', phone='12345678901',
                    lecture_theme='Pythonico')
        self.resp = self.client.post(r('subscription:subscription'), data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/1/"""
        self.assertRedirects(self.resp,
                             r('subscription:subscription-detail', 1))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())
    

class SubscriptionCreatePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('subscription:subscription'))
    
    def test_post(self):
        """Invalid Post should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscription/subscription_added.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(name='Victor Hugo', cpf='12345678901',
                            lecture_theme='python')
        resp = self.client.post(r('subscription:subscription'), invalid_data)

        self.assertContains(resp, '<ul class="errorlist nonfield">')
