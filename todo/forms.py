from django import forms
from .models import Todo
from django.forms import *


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter you Title'
                }),
            'details': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Enter you Task'
                }),

            'date':DateTimeInput(attrs={
                'class':'form-control',
            })

            
        
        }

class UpdateFrom(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'


        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Enter you Title'
                }),
            'details': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Enter you Task'
                }),

            'date':DateTimeInput(attrs={
                'class':'form-control',
            })

            
        
        }


    
        
        
        