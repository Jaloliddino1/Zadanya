# business/forms.py
from django import forms
from .models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['name', 'brand', 'price', 'stock']
