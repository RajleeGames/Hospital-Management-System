from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

def patient_list(request):
    patients = Patient.objects.all().order_by('-created_at')
    return render(request, 'patients/patient_list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        print("POST Data:", request.POST)  # Debug print
        if form.is_valid():
            print("Form is valid. Saving patient...")
            form.save()
            return redirect('patient_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})
