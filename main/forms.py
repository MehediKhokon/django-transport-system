import datetime
import mapbox_location_field
from django import forms
from main import models
from django.core.exceptions import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
	booking_start_date = forms.DateInput()
	booking_end_date = forms.DateInput()

	class Meta:
	    model = models.Booking
	    fields = ('car', 'booking_start_date', 'booking_end_date',)
	    widgets = {'booking_start_date': DateInput(), 'booking_end_date': DateInput()}

	def clean_booking_start_date(self):
		data = self.cleaned_data['booking_start_date']
		if data < datetime.date.today():
			raise ValidationError('Invalid date')

		return data
	
	def clean_booking_end_date(self):
		data = self.cleaned_data['booking_end_date']
		if data < datetime.date.today():
			raise ValidationError('Invalid date')

		return data	    
    

class RideForm(forms.ModelForm):
    class Meta:
        model = models.Ride
        fields = ('origin', 'destination',)
