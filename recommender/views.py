import os
import joblib
import pandas as pd
import json
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import PredictionForm
from .models import PredictionHistory

# Paths to the machine learning files relative to BASE_DIR (E:\INTERN PROJECT\project)
MODEL_PATH = os.path.join(settings.BASE_DIR, "crop_recommend_model")
ENCODERS_PATH = os.path.join(settings.BASE_DIR, "crop_recommend_encoders")



# Helper to automatically seed a default administrator if database is empty
def check_and_create_default_admin():
    if not User.objects.exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@agrigrow.com',
            password='adminpassword',
            first_name='Agriculture',
            last_name='Admin'
        )

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def dispatch(self, request, *args, **kwargs):
        check_and_create_default_admin()
        if request.user.is_authenticated:
            return redirect('prediction_dashboard')
        return super().dispatch(request, *args, **kwargs)

@login_required
def prediction_dashboard(request):
    prediction_result = None
    error_message = None
    
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            try:
                # 1. Gather inputs
                n = form.cleaned_data['n']
                p = form.cleaned_data['p']
                k = form.cleaned_data['k']
                temp = form.cleaned_data['temperature']
                humidity = form.cleaned_data['humidity']
                ph = form.cleaned_data['ph']
                rainfall = form.cleaned_data['rainfall']
                
                # 2. Check if model files exist
                if not os.path.exists(MODEL_PATH) or not os.path.exists(ENCODERS_PATH):
                    raise FileNotFoundError(f"Model or Encoder files could not be located in {settings.BASE_DIR}")
                
                # 3. Load ML model and encoders
                model = joblib.load(MODEL_PATH)
                encoders = joblib.load(ENCODERS_PATH)
                
                # 4. Format features as a pandas DataFrame matching original columns
                features = pd.DataFrame([{
                    'N': float(n),
                    'P': float(p),
                    'K': float(k),
                    'temperature': float(temp),
                    'humidity': float(humidity),
                    'ph': float(ph),
                    'rainfall': float(rainfall)
                }])
                
                # 5. Predict using the decision tree classifier
                pred_encoded = model.predict(features)[0]
                
                # 6. Decode output crop label using the fit encoders
                if 'label' in encoders:
                    label_encoder = encoders['label']
                    predicted_crop = label_encoder.inverse_transform([pred_encoded])[0]
                else:
                    # Fallback if label encoder key isn't formatted as expected
                    first_encoder = list(encoders.values())[0]
                    predicted_crop = first_encoder.inverse_transform([pred_encoded])[0]
                
                # Convert crop label to readable title case
                predicted_crop = str(predicted_crop).title()
                
                # 7. Save prediction record to DB history
                prediction_instance = form.save(commit=False)
                prediction_instance.user = request.user
                prediction_instance.predicted_crop = predicted_crop
                prediction_instance.save()
                
                prediction_result = predicted_crop
                form = PredictionForm()  # Reset form
                
            except Exception as e:
                error_message = f"ML Engine Error: {str(e)}"
    else:
        form = PredictionForm()
        
    # Retrieve past predictions for this authenticated user
    history = PredictionHistory.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'form': form,
        'prediction_result': prediction_result,
        'error_message': error_message,
        'history': history,
    }
    return render(request, 'recommender/dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@require_POST
def update_prediction_status(request):
    try:
        data = json.loads(request.body)
        prediction_id = data.get('id')
        new_status = data.get('status')
        if new_status not in ['Recommended', 'Cultivation', 'Harvested']:
            return JsonResponse({'success': False, 'error': 'Invalid status'}, status=400)
        
        prediction = PredictionHistory.objects.get(id=prediction_id, user=request.user)
        prediction.status = new_status
        prediction.save()
        return JsonResponse({'success': True})
    except PredictionHistory.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Record not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)


@login_required
def crop_dataset_view(request):
    csv_path = os.path.join(settings.BASE_DIR, "Crop_recommendation.csv")
    summary_data = []
    sample_data = []
    crop_counts = {}
    total_records = 0
    
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)
            total_records = len(df)
            summary = df.groupby('label').mean().reset_index()
            summary_data = summary.to_dict(orient='records')
            crop_counts = df['label'].value_counts().to_dict()
            sample_data = df.sample(n=min(250, total_records), random_state=42).to_dict(orient='records')
        except Exception as e:
            print(f"Error loading csv: {e}")
            
    context = {
        'summary_data_json': json.dumps(summary_data),
        'sample_data_json': json.dumps(sample_data),
        'crop_counts_json': json.dumps(crop_counts),
        'total_records': total_records,
        'crop_names': list(crop_counts.keys())
    }
    return render(request, 'recommender/crop_dataset.html', context)


@login_required
def ml_analytics_view(request):
    feature_importance = []
    if os.path.exists(MODEL_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            if hasattr(model, 'feature_importances_'):
                features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
                importances = model.feature_importances_.tolist()
                feature_importance = [{'feature': f, 'importance': imp} for f, imp in zip(features, importances)]
                feature_importance = sorted(feature_importance, key=lambda x: x['importance'], reverse=True)
        except Exception as e:
            print(f"Error loading model details: {e}")
            
    history = PredictionHistory.objects.filter(user=request.user)
    total_predictions = history.count()
    
    crop_stats = {}
    status_stats = {'Recommended': 0, 'Cultivation': 0, 'Harvested': 0}
    for item in history:
        crop_stats[item.predicted_crop] = crop_stats.get(item.predicted_crop, 0) + 1
        status_stats[item.status] = status_stats.get(item.status, 0) + 1
        
    context = {
        'feature_importance_json': json.dumps(feature_importance),
        'total_predictions': total_predictions,
        'crop_stats_json': json.dumps(crop_stats),
        'status_stats_json': json.dumps(status_stats)
    }
    return render(request, 'recommender/ml_analytics.html', context)

