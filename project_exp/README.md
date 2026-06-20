# AgriGrow - Crop Recommendation Engine & Cultivation Tracker

AgriGrow is a modern, responsive web application built with **Django (Python)** and **MySQL** that suggests the most suitable crops for cultivation based on soil and weather environmental parameters. It utilizes a trained **Decision Tree Classifier** machine learning model to classify inputs in real-time, and integrates a premium **Glassmorphism / Depth UI** dashboard featuring a **Bento Grid** layout and an interactive **Kanban Cultivation Board**.

---

## 📂 Project Structure Overview

Here is an architectural map of the project files and directories:

```text
E:\INTERN PROJECT\project\
│
├── manage.py                     # Django administrative command-line utility
├── db.sqlite3                    # Deprecated SQLite database (migrated to MySQL)
├── Crop_recommendation.csv       # Training dataset used for the ML Model
├── crop_prediction_confusion_matrix.png  # Performance metric plot of the ML Model
├── crop_recommender_model.py     # Python script used to train and pickle the ML model
├── crop_recommend_model          # Saved/serialized trained Decision Tree model file (joblib)
├── crop_recommend_encoders       # Serialized label encoders mapping crop strings to indices
│
├── agri_portal/                  # Core Project Configuration Directory
│   ├── __init__.py               # Package initialization (configures PyMySQL backend)
│   ├── settings.py               # Application settings, database config, and middlewares
│   ├── urls.py                   # Root URL configuration routing to apps
│   ├── asgi.py & wsgi.py         # Server interface entry points
│
├── recommender/                  # Custom Django App (Business Logic & ML)
│   ├── models.py                 # Database models defining crop records and status
│   ├── views.py                  # Controllers handling requests, ML predictions, and AJAX
│   ├── forms.py                  # ModelForm handling user input validations and placeholders
│   ├── urls.py                   # App routing mapping dashboard views & status endpoints
│   └── migrations/               # Database schema version histories
│
├── static/                       # Static Asset Folders
│   ├── css/
│   │   └── styles.css            # Stylesheet containing Glassmorphism, Bento Grid & Kanban styles
│   └── images/
│       └── agri_bg.jpg           # Generated premium sunset agriculture background image
│
└── templates/                    # HTML Presentation Layer
    ├── base.html                 # Core layout structure (navigation navbar, scripts setup)
    ├── recommender/
    │   └── dashboard.html        # Bento Grid dashboard & interactive Kanban script
    └── registration/
        └── login.html            # Translucent glassmorphism login interface
```

---

## 🔍 Segment-Wise Code Explanation

### 1. Database Integration Segment (`MySQL`)
Originally configured to use SQLite, the project has been updated to connect to a **MySQL / MariaDB database** named `crop_recommendation` hosted locally.

*   **`agri_portal/__init__.py`**:
    Since Django requires a compatible client for MySQL, we import `pymysql` and run `pymysql.install_as_MySQLdb()` to make python treat it as a drop-in replacement for `mysqlclient`.
*   **`agri_portal/settings.py`**:
    The default database configuration is modified to point to the local MySQL server:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'crop_recommendation',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    ```
    All prediction entries, dashboard statistics, user data, and authentication parameters are stored directly in this database.

---

### 2. Machine Learning Engine Segment
The application uses a trained Decision Tree Classifier to predict the ideal crop.

*   **`crop_recommender_model.py`**:
    The script that parses the `Crop_recommendation.csv` dataset, fits a Decision Tree, encodes the target column (`label` representing the crops), and serializes the assets.
*   **Model Loading (`recommender/views.py` Lines 55–85)**:
    Whenever the environmental inputs form is submitted:
    1.  Checks if the model files exist on the filesystem (`crop_recommend_model` and `crop_recommend_encoders`).
    2.  Loads both serialized binary files using `joblib.load()`.
    3.  Formats the seven environmental inputs (`N`, `P`, `K`, `temperature`, `humidity`, `ph`, `rainfall`) as a 2D Pandas DataFrame matching the original training columns.
    4.  Feeds the dataframe to `model.predict()`, producing an encoded index.
    5.  Passes the index through the label encoder's `inverse_transform()` function to decode the crop back into a readable string (e.g., "rice" becomes "Rice").

---

### 3. Business Logic & Model Schema Segment (`recommender/`)

This directory represents the core application containing the database tables and request controllers.

#### 📁 `recommender/models.py`
Defines the `PredictionHistory` database model mapping to the database table.
*   **Fields**:
    *   `user`: ForeignKey linking the prediction to a specific authenticated user.
    *   `n`, `p`, `k`: Float numbers representing Nitrogen, Phosphorus, and Potassium.
    *   `temperature`, `humidity`, `ph`, `rainfall`: Climatic and soil acidity details.
    *   `predicted_crop`: The string output classification recommended by the machine learning model.
    *   `status`: Used for the **Kanban Tracker** layout columns. It has choices: `Recommended`, `Cultivation` (representing active cultivation), and `Harvested`.
    *   `created_at`: DateTime log tracking when the computation was performed.

#### 📁 `recommender/forms.py`
Constructs the form using Django's form wrapper. It inherits from `PredictionHistory` and applies custom CSS classes (`form-control`) and placeholders to form inputs to match our UI theme.

#### 📁 `recommender/views.py`
Controls page routing and contains three main request functions:
1.  **`CustomLoginView`**: Checks if any administrator exists, creates a default admin (`admin` / `adminpassword`) on the fly if empty, and authenticates administrative credentials.
2.  **`prediction_dashboard`**: Fired on both GET and POST requests.
    *   *GET*: Queries the logged-in user's past predictions from the database (`PredictionHistory.objects.filter(user=request.user)`) and renders the dashboard.
    *   *POST*: Validates form inputs, runs the ML classification logic, stores the resulting parameters and output crop into the MySQL database with status set to `'Recommended'`, and clears the input form.
3.  **`update_prediction_status`**: Fires on POST request from frontend Javascript fetch events. Reads JSON values (`id` of prediction, `status` stage), updates the corresponding row in the MySQL database, and returns a JSON response: `{'success': True}`.

---

### 4. Frontend Interface Theme Segment (Glassmorphism, Bento, and Kanban)

The presentation layer is designed to look modern and premium, shifting away from generic layouts to a high-fidelity visual experience.

#### 🎨 Custom Stylesheet (`static/css/styles.css`)
*   **Glassmorphism & Depth UI**: Styled cards using a combination of semi-transparent background color (`rgba(10, 22, 12, 0.42)`), background blur saturation (`backdrop-filter: blur(16px)`), a subtle white translucent border (`rgba(255, 255, 255, 0.08)`), and multiple box-shadow layers. Added a glowing transition effect on hover that scales and shifts cards upward (`transform: translateY(-4px)`).
*   **Theme Background**: Set up a full-page background featuring a custom generated high-definition sunrise agricultural image (`/static/images/agri_bg.jpg`) covered by a dark, green-tinted radial gradient to ensure text readability and element contrast.
*   **Bento Grid**: Uses a CSS grid system allocating elements to a 12-column template:
    *   System Banner: Spans 12 columns.
    *   Inputs Form: Spans 5 columns.
    *   ML Recommendation Output: Spans 3 columns.
    *   optimal Guidelines Board: Spans 4 columns.
    *   Kanban Cultivation Board: Spans 12 columns at the bottom.
*   **Kanban Boards Layout**: Custom flex grid columns representing:
    *   **Recommended**: Light-bulb icon, green color accents.
    *   **Cultivating**: Shovel icon, orange/amber color accents.
    *   **Harvested**: Check-circle icon, blue color accents.

#### 🖥️ Dashboard Page Template (`templates/recommender/dashboard.html`)
Presents the Bento Grid elements and includes an asynchronous Kanban controller:
*   **Template Filtering**: Past predictions query results are dynamically filtered into columns using Django conditionals:
    ```html
    {% if item.status == 'Recommended' %} <!-- Render card in column 1 --> {% endif %}
    {% if item.status == 'Cultivation' %} <!-- Render card in column 2 --> {% endif %}
    ```
*   **Asynchronous Transitions (AJAX)**:
    When a button (e.g., *Cultivate* or *Harvest*) is clicked, the `transitionCard(id, status)` function is executed:
    1.  Dispatches a POST request to `update-status/` containing the record ID and new stage status, alongside the authenticated `X-CSRFToken` header.
    2.  If the backend MySQL updates successfully, the script triggers a CSS transition fading out the card (`opacity = 0`, `scale = 0.85`).
    3.  Moves the card element inside the DOM tree under the new status column container.
    4.  Updates card theme colors, action buttons, and icons dynamically using Lucide.
    5.  Executes a smooth entry fade-in animation and recalculates the header count badges.

---

## 🚀 Getting Started & Execution Guide

Follow these steps to run the application on your local machine:

### Prerequisites
1.  **Python**: Ensure Python (version 3.9 to 3.12 recommended) is installed.
2.  **MySQL Server**: Ensure MySQL or MariaDB (e.g., XAMPP, WAMP, or standalone MySQL) is running locally.

### Setup Steps
1.  **Configure MySQL Database**:
    *   Open phpMyAdmin or your MySQL terminal.
    *   Create a database named **`crop_recommendation`**:
        ```sql
        CREATE DATABASE crop_recommendation;
        ```
2.  **Activate Virtual Environment**:
    *   Open your command prompt or terminal in the project directory (`E:\INTERN PROJECT\project`).
    *   Activate the existing virtual environment:
        ```cmd
        .venv\Scripts\activate
        ```
3.  **Install Required Dependencies**:
    *   Ensure all necessary packages (Django, PyMySQL, pandas, scikit-learn, joblib) are installed:
        ```bash
        pip install django<5.1 pymysql pandas scikit-learn joblib
        ```
4.  **Perform Database Migrations**:
    *   Generate and apply the tables schema mapping to your MySQL database:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```
5.  **Run Development Server**:
    *   Launch the local Django server:
        ```bash
        python manage.py runserver
        ```
    *   Open your web browser and navigate to: `http://127.0.0.1:8000/`

### 🔑 Default Credentials
When loading the database for the first time, a default administrator is seeded automatically:
*   **Username**: `admin`
*   **Password**: `adminpassword`
