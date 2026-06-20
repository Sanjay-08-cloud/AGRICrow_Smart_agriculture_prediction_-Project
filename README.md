# 🌾 AgriGrow - Crop Recommendation Engine & Cultivation Tracker

AgriGrow is a modern, enterprise-grade web application designed to help farmers and agronomists optimize crop yields. By analyzing key environmental metrics (nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall), the application suggests the most suitable crops for cultivation using a real-time **Decision Tree Classifier** machine learning model.

The frontend features a high-fidelity **Glassmorphism / Depth UI** dashboard with a **Bento Grid** layout, interactive data visualizations, and an agile **Kanban Cultivation Board** to track crops from recommendation to harvest.

---

## 🛠️ Tech Stack & Architecture

- **Backend Framework**: Django (Python 3.9+)
- **Machine Learning**: Scikit-Learn (Decision Tree Classifier), Pandas, NumPy, Joblib
- **Database**: 
  - **Local Development**: SQLite (Default `db.sqlite3` file) or MySQL
  - **Production/Cloud**: PostgreSQL (via `dj-database-url` integration)
- **Frontend / Styling**: Vanilla CSS (Glassmorphism, Bento Grid, Kanban layouts), HTML5, Lucide Icons, and responsive design.
- **Production Server**: Gunicorn / WhiteNoise (for static file serving)

---

## 📂 Project Directory Structure

```text
E:\INTERN PROJECT\project\
│
├── manage.py                     # Django administrative entry-point
├── db.sqlite3                    # Local SQLite database (used for development)
├── Crop_recommendation.csv       # Training dataset for the ML model (2200 rows)
├── crop_recommender_model.py     # Python script to train, evaluate, and save the ML model
├── crop_recommend_model          # Serialized Decision Tree model file (joblib)
├── crop_recommend_encoders       # Serialized label encoders (joblib)
├── crop_prediction_confusion_matrix.png  # ML performance metric visualization
├── requirements.txt              # Project packages & production server dependencies
├── .gitignore                    # Version control exclusion rules
│
├── agri_portal/                  # Core Project Configuration Directory
│   ├── __init__.py               # Package init & MySQL client mapping setup
│   ├── settings.py               # Application configurations (Production-ready environment load)
│   ├── urls.py                   # Root URL routing configurations
│   ├── asgi.py & wsgi.py         # ASGI/WSGI deployment hook entry-points
│
├── recommender/                  # Custom Django App (Core Logic & ML Integration)
│   ├── models.py                 # DB models mapping prediction history & Kanban states
│   ├── views.py                  # Controllers for pages, AJAX endpoints, & ML predictions
│   ├── forms.py                  # ModelForm handling user environmental input styling
│   ├── urls.py                   # App routing mapping dashboard views & status endpoints
│   └── migrations/               # Database schema version histories
│
├── static/                       # Static Assets
│   ├── css/
│   │   └── styles.css            # Premium Glassmorphism & Bento Grid UI stylesheet
│   └── images/
│       └── agri_bg.jpg           # Premium sunset agricultural background image
│
└── templates/                    # HTML Templates
    ├── base.html                 # Main layout wrapper (navigation navbar, static script hooks)
    ├── recommender/
    │   ├── dashboard.html        # Interactive Bento Grid dashboard & Kanban Kanban columns
    │   ├── crop_dataset.html     # Dataset visualization page
    │   └── ml_analytics.html     # ML model feature importance & metrics analysis page
    └── registration/
        └── login.html            # Translucent glassmorphism login interface
```

---

## ⚙️ Local Development Setup

To run AgriGrow locally:

### 1. Prerequisites
- **Python 3.9+** installed on your system.
- Git (optional, for pushing to GitHub).

### 2. Configure Virtual Environment
Open your command prompt or terminal in the project directory (`E:\INTERN PROJECT\project`):
```cmd
# Create virtual environment if not already present
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Initialization (SQLite default)
```bash
# Generate database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 5. Start Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

### 🔑 Default Credentials
On database initialization, a default administrator account is automatically seeded:
- **Username**: `admin`
- **Password**: `adminpassword`

---

## ☁️ Production Deployment

AgriGrow is optimized for cloud platforms like **Render**, **Railway**, or **Heroku**. It supports standard WSGI servers, auto-detects cloud databases via `DATABASE_URL`, and manages static files using WhiteNoise.

### Environmental Variables
Before deploying, set the following environment variables in your cloud provider:

| Variable Name | Description | Recommended Production Value |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | Private cryptographic key for Django | A long random string |
| `DJANGO_DEBUG` | Django debug toggle | `False` |
| `ALLOWED_HOSTS` | Trusted domains hosting the app | `your-app-domain.onrender.com` |
| `DATABASE_URL` | Cloud Database connection string | `postgres://user:password@host:port/database` |

### Deploying to Render (Recommended & Free)
1. **Create a Web Service** on [Render](https://render.com/).
2. Connect your Git repository.
3. Configure the environment:
   - **Runtime**: `Python`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn agri_portal.wsgi`
4. Set up a **Render PostgreSQL database** (or any other hosted PostgreSQL like Neon/Supabase), copy the connection string, and set it as `DATABASE_URL` in the environment variables of your Render Web Service.

---

## 📊 Machine Learning Model Details

The crop recommendation logic relies on a **Decision Tree Classifier** trained on the `Crop_recommendation.csv` dataset. 
- **Features Used**: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, Soil pH, and Rainfall.
- **Target Label**: Classification mapping to 22 different crop categories (e.g. Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas, Mothbeans, Mungbean, Blackgram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee).
- **Training Script**: Run `python crop_recommender_model.py` to retrain the model and save newer weights.
