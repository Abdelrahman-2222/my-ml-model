from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class HeartDisease(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    HighBP = models.BooleanField()
    HighChol = models.BooleanField()
    CholCheck = models.BooleanField()
    BMI = models.IntegerField(
        validators=[
            MinValueValidator(10),
            MaxValueValidator(50),
        ]
    )
    Smoker = models.BooleanField()
    Stroke = models.BooleanField()
    DIABETES_CHOICES = (
        (0, 'NO'),
        (1, 'Type 1'),
        (2, 'Type 2'),
    )
    Diabetes = models.IntegerField(choices=DIABETES_CHOICES)
    PhysActivity = models.BooleanField()
    Veggies = models.BooleanField()
    NoDocbcCost = models.BooleanField()
    GenHlth = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    MentHlth = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    PhysHlth = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    DiffWalk = models.BooleanField()
    SEX_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    Sex = models.CharField(choices=SEX_CHOICES, max_length=1)
    Age = models.IntegerField()
    Education = models.IntegerField()
    Income = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    result = models.BooleanField(null=True)
    submitted_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name