from django.contrib import admin
from django.urls import path
from app.views import DoctorListCreate, DoctorRetrieveUpdateDelete

urlpatterns = [
    path('admin/', admin.site.urls),

    # GET all doctors + POST new doctor
    path('doctor/', DoctorListCreate.as_view(), name='doctor-list-create'),

    # GET one + PUT update + DELETE doctor
    path('doctor/<int:id>/', DoctorRetrieveUpdateDelete.as_view(), name='doctor-detail'),
]