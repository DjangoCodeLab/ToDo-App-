from django import forms
from django.contrib.auth.models import User
from accounts.models import User_account


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class':'form-control'
        }
    ))
    password2 = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            'class':'form-control'
        }
    ),label="confirm password")


    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username':forms.TextInput(attrs = {
                'class':'form-control'
            }),
            'email':forms.EmailInput(attrs = {
                'class':'form-control'
            }),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password']!= cd['password2']:
            raise forms.ValidationError('password don\'t match.')
        
        return cd['password2']
    

    
class UserAccountForm(forms.ModelForm):
    class Meta:
        model = User_account
        fields = [
            'phone_number',
            'address',
            'date_of_birth', 
            'profile_picture'
        ]

        widgets ={
            'phone_number':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'address':forms.Textarea(attrs = {
                'class':'form-control'
            }),
            'date_of_birth':forms.DateInput(attrs = {
                'class':'form-control',
                'type':'date'
            }),
            'profile_picture':forms.FileInput(attrs = {
                'class':'form-control'
            }),


        }

class LoginForm(forms.Form):
    class Meta:
        method = User
        fields = ['username', 'password']

        
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    