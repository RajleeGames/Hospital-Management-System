from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control datepicker',  # add a class identifier for Flatpickr
                'placeholder': 'Select a date'
            },
            format='%d/%m/%Y'
        ),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'contact_number', 'email', 'address']
