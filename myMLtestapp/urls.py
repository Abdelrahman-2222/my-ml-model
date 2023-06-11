from django.urls import path
from .api import (heart_disease_name, heart_disease_create,
                  HeartDiseaseApi, heart_disease_list, SubmitForm,
                  heart_disease_detail)

# submit_form,

app_name = 'myMLtestapp'

urlpatterns = [
    path('patients_list/', heart_disease_list, name="heart_disease_list"),
    path('fdetails/<int:pk>', heart_disease_detail, name="heart_disease_detail"),
    path('submit-form/', SubmitForm.as_view(), name="submit_form"),
    # path('submit-form/', submit_form, name="submit_formFBV"),
    path('fname/<str:name>', heart_disease_name, name="heart_disease_name"),
    path('fcreate/', heart_disease_create, name="heart_disease_create"),
    # path('Clist/<str:user_id>', HeartDiseaseApi.as_view(), name="heart_disease_c_list"),
    path('each_patient/<str:user_id>', HeartDiseaseApi.as_view(), name="heart_disease_c_list"),

]
