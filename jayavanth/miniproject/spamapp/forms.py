from django import forms
from . models import spammail

class email_form(forms.ModelForm):
    class Meta:
        model = spammail
        fields = ('Email_Body',)