from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            "class": "from-control",
            "placeholder": "Your name"
        })
        self.fields['email'].widget.attrs.update({
            "class": "from-control",
            "placeholder": "Email"
        })
        self.fields['phone'].widget.attrs.update({
            "class": "from-control",
            "placeholder": "Phone"
                })
        self.fields['message'].widget.attrs.update({
            "class": "from-control",
            "placeholder": "Message"
        })
