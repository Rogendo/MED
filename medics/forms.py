from django import forms
from medexpert.models import Msgs

class Tableform(forms.ModelForm):

    class Meta:
        model = Msgs
        fields='__all__'
