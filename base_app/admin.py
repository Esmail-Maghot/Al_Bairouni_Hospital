from django.contrib import admin

# Register your models here.
from .models import Doctors,Patient_Record,Patients,Sections

admin.site.register(Sections)
admin.site.register(Doctors)
admin.site.register(Patients)
admin.site.register(Patient_Record)