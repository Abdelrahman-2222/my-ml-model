from .models import HeartDisease
from rest_framework import serializers


class HeartSerializer(serializers.ModelSerializer):
    result = serializers.BooleanField(read_only=True)
    submitted_time = serializers.DateTimeField(format="%d %b %Y %H:%M:%S", read_only=True)

    class Meta:
        model = HeartDisease
        # fields = '__all__'
        fields = (
            'id', 'first_name', 'last_name', 'user_id', 'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
            'Diabetes', 'PhysActivity', 'Veggies', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk',
            'Sex', 'Age', 'Education', 'Income', 'result', 'submitted_time')


# 'Fruits', 'HvyAlcoholConsump', 'AnyHealthcare', ,

class HeartSerializerList(serializers.ModelSerializer):
    prediction = serializers.SerializerMethodField()
    submitted_time = serializers.SerializerMethodField()

    class Meta:
        model = HeartDisease
        fields = ['first_name', 'last_name', 'HighBP', 'HighChol', 'prediction', 'submitted_time']

    def get_prediction(self, obj):
        return obj.result

    def get_submitted_time(self, obj):
        return obj.submitted_time.strftime('%d %b %Y')
