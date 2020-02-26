from django import forms
from .models import Friend, ClassYear

CLASSYEAR = [
    ('2019','2019'),
    ('2018', '2018'),
    ('2017','2017'),
    ('2016','2016'),
    ('2015','2015'),
    ('Other','Other'),
]

class FriendForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Please enter your name',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    ClassYear = forms.CharField(widget=forms.Select(choices=CLASSYEAR))
    hobby = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'What is your hobby? (ex. Sleep)',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    food = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'What is your favorite food?',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))
    drink = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'What is your favorite drink?',
        'type' : 'text',
        'maxlength' : '255',
        'required' : True,
        'style' : 'border-radius:20px;',
        'label' : '',
    }))