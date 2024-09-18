from django import forms
from .models import Beneficiary

class BeneficiaryForm(forms.ModelForm):
    beneficiary = forms.ModelChoiceField(queryset=Beneficiary.objects.all(), widget=forms.Select(attrs={'id': 'beneficiary_select'}))

    class Meta:
        model = Beneficiary
        fields = ['beneficiary']
