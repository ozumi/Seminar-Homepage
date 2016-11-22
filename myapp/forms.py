from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput())
	email = forms.CharField(widget=forms.TextInput())
	phone = forms.CharField(widget=forms.TextInput())
	affilliation = forms.CharField(widget=forms.TextInput())
	department = forms.CharField(widget=forms.TextInput())
	position = forms.CharField(widget=forms.TextInput())

	class Meta:
		model = Register
		fields = ()

