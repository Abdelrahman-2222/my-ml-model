from django.urls import path
from .api import (heart_disease_name, heart_disease_create,
                  HeartDiseaseApi, SubmitForm, heart_disease_list,
                  heart_disease_detail)

app_name = 'myMLtestapp'

urlpatterns = [
    path('flist/', heart_disease_list, name="heart_disease_list"),
    path('fdetails/<int:pk>', heart_disease_detail, name="heart_disease_detail"),
    path('submit-form/', SubmitForm.as_view(), name="submit_form"),
    path('fname/<str:name>', heart_disease_name, name="heart_disease_name"),
    path('fcreate/', heart_disease_create, name="heart_disease_create"),
    path('Clist/<int:id>', HeartDiseaseApi.as_view(), name="heart_disease_c_list"),
]