from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datepicker',
                'placeholder': 'Select appointment date'
            },
            format='%d/%m/%Y'
        ),
        input_formats=['%d/%m/%Y']
    )
    
    class Meta:
        model = Appointment
        fields = '__all__'
