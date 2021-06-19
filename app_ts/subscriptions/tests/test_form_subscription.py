from django.test import TestCase

from app_ts.subscriptions.validators import validate_cpf

from app_ts.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 5 fields."""
        form = SubscriptionForm()
        expected = ['name',
                    'cpf',
                    'email',
                    'phone',
                    'lecture_theme']
        self.assertSequenceEqual(['name',
                                  'cpf',
                                  'email',
                                  'phone',
                                  'lecture_theme'], list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accpet digits."""
        form = self.make_validated_form(cpf='abc5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11  digits."""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """Name must be capitalized."""
        form = self.make_validated_form(name='Victor hugo')
        self.assertEqual('Victor Hugo', form.cleaned_data['name'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Victor Hugo', cpf='12345678901',
                     email='victor-hugopy@outlook.com', phone='81-998832982')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

