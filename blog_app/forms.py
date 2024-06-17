from django import forms
from django.core.validators import ValidationError

from blog_app.models import Message

class ContactUsForm(forms.Form):
    birth_choices = ['1998','1999','2000']
    text = forms.CharField(max_length=10,label='your message')
    name = forms.CharField(max_length=10,label='your name')
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=birth_choices))



    def clean(self):
        name =self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same',code='name_text_same')



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message 
        fields = '__all__'