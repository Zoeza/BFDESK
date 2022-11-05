from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['client_reg']
        widgets = {
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'client_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'client_gender': forms.Select(attrs={'class': 'form-control'}),
            'client_date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'client_lawyer': forms.TextInput(attrs={'class': 'form-control'}),
            'client_address': forms.TextInput(attrs={'class': 'form-control'}),

        }
