
from django import forms
from django.contrib.auth.models import User
# from django.core.validators import ValidationError
from django.core.exceptions import ValidationError
from. models import Message , Ticket


class ContactUsForm(forms.Form):
    BIRTH_YEAR_CHOICES=[1995,1996,1997,1998,1999,2000]
    name=forms.CharField(max_length=500,label='your name')
    message=forms.CharField(max_length=500,label='your message')
    birthday=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    
    def clean(self):
        name=self.cleaned_data.get('name')
        message=self.cleaned_data.get('message')
        if name == message :
            print('error')
            raise ValidationError('your name and message are same!', code='name_message_same')
        else:print('right')
    
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if 'a' in name:
            print('error')
            raise ValidationError('your name can not have "a" !!',code='a in neme')
        return name
    
    
    
    
class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['title','text','email']
    


class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields=['title','text']
    
    
class SetEmail(forms.ModelForm):
    class Meta:
        model=User
        fields=['email']
    