from django import forms
from .models import Contact

class Contact_BerichtForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone',
            'message'
        ]
