from django.forms import ModelForm
from mainsite import models
from django import forms

class ContactUsForm(ModelForm):
    class Meta():
        model = models.Contact_Us
        fields = ['name', 'email', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name', 'class':'fields field name', 'type':'text'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class':'fields field email', 'type':'email'}),
            'message': forms.Textarea(attrs={'placeholder':'Message...', 'class':'field textarea', 'type':'textarea', 'cols':'50', 'row':'10'})
        }