from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MemberInfo(models.Model):

    GOALS = [
        ('Lose weight', 'Lose weight'),
        ('Maintain weight', 'Maintain weight'),
        ('Gain weight', 'Gain weight'),
        ('Gain muscle', 'Gain muscle'),
    ]

    SEXES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    ACTIVITY_LEVELS = [
        ('Sedentary', 'Sedentary'),
        ('Lightly active', 'Lightly active'),
        ('Moderately active', 'Moderately active'),
        ('Very  active', 'Very active'),
        ('Extra active', 'Extra active'),
    ]

    memberid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=255, choices=GOALS)
    sex = models.CharField(max_length=255, choices=SEXES)
    age = models.IntegerField(default=18)
    height = models.IntegerField(default=150)
    weight = models.FloatField(default=50)
    weight_goal = models.FloatField(default=50)
    activity_level = models.CharField(max_length=255, choices=ACTIVITY_LEVELS)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def calculate_bmr(self):
        # Calculates the user's Basal Metabolic Rate (BMR).
        if self.sex == 'Male':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.sex == 'Female':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return bmr
    
    def calculate_tdee(self):
        # Calculates the user's Total Daily Energy Expenditure (TDEE).
        bmr = self.calculate_bmr()
        if self.activity_level == "Sedentary":
            tdee = bmr * 1.2
        if self.activity_level == "Lightly active":
            tdee = bmr * 1.375
        if self.activity_level == "Moderately active":
            tdee = bmr * 1.55
        if self.activity_level == "Very active":
            tdee = bmr * 1.725
        if self.activity_level == "Extra active":
            tdee = bmr * 1.9
        return tdee
    
    def calculate_bmi(self):
        height_meters = self.height / 100
        bmi = self.weight / (height_meters ** 2)
        return bmi