from django import forms
from .models import PredictionHistory

class PredictionForm(forms.ModelForm):
    class Meta:
        model = PredictionHistory
        fields = ['n', 'p', 'k', 'temperature', 'humidity', 'ph', 'rainfall']
        widgets = {
            'n': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nitrogen (N) e.g. 50', 'step': 'any'}),
            'p': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phosphorus (P) e.g. 35', 'step': 'any'}),
            'k': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Potassium (K) e.g. 120', 'step': 'any'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Temperature (°C) e.g. 24.5', 'step': 'any'}),
            'humidity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Humidity (%) e.g. 62.8', 'step': 'any'}),
            'ph': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'pH Level (0-14) e.g. 6.5', 'step': 'any'}),
            'rainfall': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rainfall (mm) e.g. 200.4', 'step': 'any'}),
        }
