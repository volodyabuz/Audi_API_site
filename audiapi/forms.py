from django import forms
from .models import *

# CAR_MODEL_CHOICES = CarModels.objects.all()

class CarForm(forms.Form):
    # car = forms.CharField(label='Выберите модель', widget=forms.Select(choices=CAR_MODEL_CHOICES))
    car = forms.ModelChoiceField(queryset=CarModels.objects.all())