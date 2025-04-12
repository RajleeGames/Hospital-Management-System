from django.contrib import admin
from django.urls import path, include
from hospital_system.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('appointments/', include('appointments.urls')),
    # Homepage URL: ""
    path('', home, name='home'),
]
