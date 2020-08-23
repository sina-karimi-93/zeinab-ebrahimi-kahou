from django import forms
from .models import ContactMe


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ('name', 'email', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Full Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }
