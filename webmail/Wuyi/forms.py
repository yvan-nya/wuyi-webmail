from dataclasses import field
from pyexpat import model
from django import forms
from Wuyi.models import Client

class Clientform(forms.ModelForm):
    file = forms.FileField(required=False)
    class Meta:
        model = Client
        fields = "__all__"