from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from dabber.models import Dabber
from captcha.fields import CaptchaField

class RegistrationForm(ModelForm):
        username        = forms.CharField(label=(u'User Name'))
        email           = forms.EmailField(label=(u'Email Address'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
        password1       = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
	captcha 	= CaptchaField()

        class Meta:
                model = Dabber
                exclude = ('user',)
                fields = ('birthday', 'email')
        def clean_username(self):
                username = self.cleaned_data['username']
                try:
                        User.objects.get(username=username)
                except User.DoesNotExist:
                        return username
                raise forms.ValidationError("That Dabber name is already taken, please take a dab then choose another.")

        def clean(self):
                if self.cleaned_data['password'] != self.cleaned_data['password1']:
                        raise forms.ValidationError("The passwords did not match. Please take two dabs and try again.")
                return self.cleaned_data

class LoginForm(forms.Form):
        username        = forms.CharField(label=(u'User Name'))
        password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))

