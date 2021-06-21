from django import forms
from django.core.exceptions import ValidationError

from app_ts.subscriptions.models import Subscription
from app_ts.subscriptions.validators import validate_cpf


class SubscriptionFormOld(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='E-mail', required=False)
    phone = forms.CharField(label='Telefone', required=False)
    lecture_theme = forms.CharField(label='Nome')


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = [
            'name',
            'cpf',
            'email',
            'phone',
            'lecture_theme'
        ]

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') \
           and not self.cleaned_data.get('phone'):
            raise ValidationError(
                'Informe seu e-mail ou telefone.'
            )

        return self.cleaned_data
