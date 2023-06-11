from django.utils import timezone
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import HeartSerializer, HeartSerializerList
from rest_framework import status
from rest_framework.response import Response
import joblib
from .models import HeartDisease
from django.db.models.signals import post_save
from django.dispatch import receiver
import numpy as np


@api_view(['GET'])
def heart_disease_list(request):
    heart_disease_objects = HeartDisease.objects.all()
    serializer = HeartSerializer(heart_disease_objects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class SubmitForm(generics.CreateAPIView):
    serializer_class = HeartSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create a new HeartDisease instance with the input data
        heart_disease = HeartDisease(**serializer.validated_data)

        # Set the submitted_time field explicitly
        heart_disease.submitted_time = timezone.now()

        # Save the instance, which will trigger the apply_nn_model signal handler
        heart_disease.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@receiver(post_save, sender=HeartDisease)
def apply_MLP_model(sender, instance, created, **kwargs):
    if created:
        # Load the saved model
        model = joblib.load('myMLtestapp/savedModels/MLP_model.joblib')

        # Prepare the input data
        X = np.array(
            [[instance.HighBP, instance.HighChol, instance.CholCheck, instance.BMI, instance.Smoker,
              instance.Stroke, instance.Diabetes, instance.PhysActivity, instance.Veggies,
              instance.NoDocbcCost, instance.GenHlth, instance.MentHlth, instance.PhysHlth, instance.DiffWalk,
              1 if instance.Sex == 'M' else 0, instance.Age, instance.Education, instance.Income]])

        # Make the prediction
        predicted_value = model.predict(X)
        threshold = 0.5
        result = predicted_value >= threshold

        # Set the predicted result
        instance.result = result
        instance.save()


@api_view(['GET'])
def heart_disease_detail(request, pk):
    try:
        heart_disease_itself = HeartDisease.objects.get(id=pk)
    except HeartDisease.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = HeartSerializer(heart_disease_itself)
    return Response(serializer.data, status=status.HTTP_200_OK)


# create a serializer api to get specific data by first_name
@api_view(['GET'])
def heart_disease_name(request, name):
    try:
        heart_disease_n = HeartDisease.objects.get(first_name=name)
    except HeartDisease.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = HeartSerializer(heart_disease_n)
    return Response(serializer.data, status=status.HTTP_200_OK)


# create a serializer api to create a new row of
@api_view(['POST'])
def heart_disease_create(request):
    serializer = HeartSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# create a serializer class api to update or delete data by id
# class HeartDiseaseApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HeartDisease.objects.all()
#     serializer_class = HeartSerializer
#     # lookup_field = 'id'
#     lookup_url_kwarg = 'id'

# class HeartDiseaseApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HeartDisease.objects.all()
#     serializer_class = HeartSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'id'

class HeartDiseaseApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HeartSerializer
    lookup_field = 'user_id'
    lookup_url_kwarg = 'user_id'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = HeartDisease.objects.filter(user_id=user_id)
        return queryset

    #
    # def get(self, request, id, user_id):
    #     heart_disease = self.get_object()  # Retrieve the HeartDisease object based on the id
    #     # Add your code to handle the GET request with the specified id and user_id
    #     # Example usage: heart_disease.user_id = user_id
    #
    #
    # def put(self, request, id, user_id):
    #     heart_disease = self.get_object()  # Retrieve the HeartDisease object based on the id
    #     # Add your code to handle the PUT request with the specified id and user_id
    #     # Example usage: heart_disease.user_id = user_id
    #
    #
    # def delete(self, request, id, user_id):
    #     heart_disease = self.get_object()  # Retrieve the HeartDisease object based on the id
    #     # Add your code to handle the DELETE request with the specified id and user_id
    #     # Example usage: if heart_disease.user_id == user_id: ... (perform deletion logic)

# # create a serializer function based view api to view patient details by id, and user_id
# @api_view(['GET'])
# def heart_disease_detail(request, pk):
#     try:
#         heart_disease_itself = HeartDisease.objects.get(id=pk)
#     except HeartDisease.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
