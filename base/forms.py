from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class booking_form(ModelForm):
    class Meta:
        model = Booking
        fields = ['roundtrip',
                  'oneway', 
                  'multi_station',
                  'departing', 
                  'destination', 
                  'departure_date', 
                  'return_date',
                  'adults', 
                  'children']
        