from django import forms
from .models import User_data,User_info


class User_form(forms.ModelForm):
    class Meta:
        model = User_data
        fields = ('username','password')
        widgets = {'password':forms.PasswordInput()}


class User_info_form(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ('dob','phone_no')