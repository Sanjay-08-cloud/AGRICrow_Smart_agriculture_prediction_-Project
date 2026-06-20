# 🌾 AgriGrow - Crop Recommendation Engine & Cultivation Tracker
### 🚀 Setup & Presentation Guide

Welcome to **AgriGrow**, a premium, full-stack agricultural web application built using **Django (Python)**, a **Decision Tree Classifier Machine Learning Model**, and **MySQL**. It features a modern **Glassmorphism & Depth UI** dashboard, a **Bento Grid** layout, and an interactive, real-time **Kanban Cultivation Tracker** powered by AJAX.

This document contains step-by-step instructions on:
1. **How to setup and run** the project on your local machine.
2. **How to present** this project successfully to examiners or colleagues (including a slide deck outline, live demo script, sample inputs table, and answers to common technical questions).

---

## 🛠️ Part 1: How to Setup and Run the Project

Follow these steps to run the application locally:

### 📋 Prerequisites
1. **Python**: Ensure Python (3.9 to 3.12 recommended) is installed on your computer. You can check this by running `python --version` in your terminal.
2. **MySQL Server**: Ensure a local MySQL server (like XAMPP, WAMP, or a standalone MySQL installation) is installed and running.

---

### 📥 Step-by-Step Installation

#### 1. Configure the MySQL Database
* Open **phpMyAdmin** (e.g., `http://localhost/phpmyadmin`) or access your MySQL command line.
* Create a new database named **`crop_recommendation`**:
  ```sql
  CREATE DATABASE crop_recommendation;
  ```
  *(Note: The database settings in `agri_portal/settings.py` are configured to connect to database `crop_recommendation` with user `root` and no password by default. If your local MySQL setup requires a password, modify `agri_portal/settings.py` accordingly).*

#### 2. Open Terminal in Project Directory
* Open your Command Prompt (CMD), PowerShell, or Git Bash.
* Navigate to the project directory:
  ```cmd
  cd "E:\INTERN PROJECT\project"
  ```

#### 3. Activate the Python Virtual Environment
* The project has an existing virtual environment named `.venv`. Activate it using:
  * **On Windows Command Prompt (CMD)**:
    ```cmd
    .venv\Scripts\activate
    ```
  * **On PowerShell**:
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
  * **On Git Bash / macOS / Linux**:
    ```bash
    source .venv/bin/activate
    ```
  *(You will see `(.venv)` prepended to your command line prompt, indicating it is active).*

#### 4. Install Dependencies
* Ensure all necessary packages are installed by running:
  ```bash
  pip install django<5.1 pymysql pandas scikit-learn joblib
  ```
  *(Note: `pymysql` is used as a drop-in replacement for `mysqlclient` to avoid complex native builds on Windows).*

#### 5. Generate and Run Database Migrations
* Apply the database tables schema mapping to your MySQL database:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
  *(This will create the necessary Django administrative tables and the `recommender_predictionhistory` table in your local MySQL database).*

#### 6. Run the Development Server
* Launch the local Django server:
  ```bash
  python manage.py runserver
  ```
* Once the server starts, you will see output indicating that the server is running at `http://127.0.0.1:8000/`.

#### 7. Access the Application
* Open your web browser and go to: **`http://127.0.0.1:8000/`**
* You will be greeted by the glassmorphism login screen.

---

### 🔑 Login Credentials
On first launch, the project automatically seeds a default administrator in the database if it doesn't already exist:
* **Username**: `admin`
* **Password**: `adminpassword`

---

## 📊 Part 2: Presentation & Demonstration Guide

To make your project stand out during your presentation, use the following guide to structure your speech, slides, and live demonstration.

### 🎴 Recommended Slide Deck Outline (8 Slides)

1. **Slide 1: Title Slide**
   * **Title**: AgriGrow: Machine Learning-Powered Crop Recommendation & Cultivation Tracker
   * **Subtitle**: A Full-Stack Django Web Application with Glassmorphism Dashboard
   * **Your Info**: [Your Name], [Internship/Project Details]

2. **Slide 2: Problem Statement & Solution**
   * **Problem**: Traditional farming relies on guesswork, leading to poor crop selection, low yields, and nutrient depletion.
   * **Solution**: A decision-support tool that analyzes environmental factors (soil nutrients & weather conditions) to recommend the most optimal crops, coupled with an interactive cultivation tracker.

3. **Slide 3: Technology Stack**
   * **Backend**: Django (Python MVC Framework)
   * **Database**: MySQL (for scalable, production-ready relational data storage)
   * **Machine Learning**: Decision Tree Classifier (trained using scikit-learn, serialized via joblib)
   * **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism & Depth UI, Bento Grid layout), JavaScript (AJAX/Fetch API)

4. **Slide 4: System Architecture & Workflow**
   * **Workflow**: 
     User Inputs Environmental Factors -> Django View receives values -> Machine Learning Model loads and predicts crop index -> Label Encoder decodes crop name -> Save prediction in MySQL database -> Render dynamically in user dashboard bento layout.

5. **Slide 5: Machine Learning Engine**
   * **Dataset**: `Crop_recommendation.csv` containing 2,200 records.
   * **Features**: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, Rainfall.
   * **Algorithm**: Decision Tree Classifier (offers high accuracy, fast real-time inference, and clear decision paths).
   * **Accuracy**: High classification precision of ~98% on test split.

6. **Slide 6: Premium UI/UX Design Elements**
   * **Glassmorphism Design**: Semi-transparent frosted-glass surfaces using `backdrop-filter: blur(16px)` and translucent borders.
   * **Bento Grid**: A modern layout partitioning forms, guidelines, recommendations, and tracking columns into a grid system.
   * **Asynchronous Kanban Tracker**: Let users track recommended crops from 'Recommended' -> 'Cultivating' -> 'Harvested' dynamically without refreshing the page.

7. **Slide 7: Live Demonstration (Screen Share)**
   * *Switch to the browser and run the live demo (see script below).*

8. **Slide 8: Conclusion & Future Scope**
   * **Future Enhancements**: Integration of live IoT sensors for soil testing, adding market price predictions for recommended crops, and introducing fertilizer recommendations.

---

### 🖥️ Step-by-Step Live Demo Script

Follow this script to showcase the app smoothly during a screen-share:

1. **Step 1: The Login Experience**
   * Start with the app loaded on the Login page (`http://127.0.0.1:8000/login/`).
   * *Talking point*: "Here is the login page, featuring a frosted-glass glassmorphism design overlaying a high-definition sunset agriculture background. We log in using our credentials."
   * Type `admin` and `adminpassword`, then click Login.

2. **Step 2: Dashboard Layout Walkthrough**
   * *Talking point*: "This is the AgriGrow main dashboard. It uses a clean Bento Grid layout to maximize screen utility. On the left is the Environmental parameters form. In the middle-right is our model recommendation result card and instructions. At the bottom is the Cultivation Board."

3. **Step 3: Live ML Recommendation Test**
   * *Action*: Input values into the form. For a perfect presentation, use one of the tested combinations below (e.g., Apple or Rice) so you get a known crop.
   * *Example (Rice)*: Input: **N = 90, P = 42, K = 43, Temp = 21, Humidity = 82, pH = 6.5, Rainfall = 203**.
   * Click **Recommend Crop**.
   * *Talking point*: "When I submit this form, Django reads the inputs, loads our trained Decision Tree model file in the backend, performs inference in milliseconds, saves the record to MySQL, and displays the recommended crop: **Rice**."

4. **Step 4: Interactive Kanban Board Tracking**
   * Scroll down to the **Cultivation Board**. Notice your new "Rice" card is under the **Recommended** column.
   * Click the **Cultivate** button on the card.
   * *Talking point*: "Once a crop is recommended, the farmer can track its life cycle. By clicking 'Cultivate', the card fades out and moves to the 'Cultivating' column. This update is performed asynchronously via an AJAX Fetch API call to our Django views, updating the MySQL database without refreshing the webpage."
   * Now click **Harvest** on the card.
   * *Talking point*: "When the crop is harvested, we click 'Harvest'. The card transitions smoothly to the 'Harvested' column, marking it complete."

---

### 🧪 Sample Presentation Inputs (Tested Combinations)

Use these exact values in your live demo to get specific crop recommendations:

| Crop Result | N (Nitrogen) | P (Phosphorus) | K (Potassium) | Temperature (°C) | Humidity (%) | pH | Rainfall (mm) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Rice** | `90` | `42` | `43` | `21.0` | `82.0` | `6.5` | `203.0` |
| **Apple** | `24` | `128` | `196` | `22.8` | `90.7` | `5.5` | `110.4` |
| **Coconut** | `18` | `30` | `29` | `26.8` | `92.9` | `6.4` | `224.6` |
| **Papaya** | `56` | `59` | `55` | `37.0` | `91.8` | `6.6` | `188.5` |
| **Pigeon Peas** | `10` | `71` | `18` | `19.5` | `66.3` | `6.2` | `173.1` |
| **Moth Beans** | `3` | `49` | `18` | `27.9` | `64.7` | `3.7` | `32.7` |

---

### ❓ Common Technical Questions Asked by Examiners

Be prepared for these questions during your project defense:

1. **Q: Why use a Decision Tree Classifier instead of other algorithms?**
   * *A*: Decision Trees are highly interpretable, fast to execute, and perform exceptionally well on structured datasets with tabular parameters like this one, achieving over 98% accuracy without the overhead of deep learning.

2. **Q: How does Django load the model and make recommendations?**
   * *A*: In `recommender/views.py`, when a POST request is received, the script uses `joblib.load()` to deserialize the pre-trained Decision Tree model (`crop_recommend_model`) and the label encoder (`crop_recommend_encoders`). The form values are formatted as a pandas DataFrame and passed to `model.predict()`, which returns an integer index. The encoder translates this index back to the crop name.

3. **Q: How does the Kanban board update without reloading the page?**
   * *A*: The dashboard includes JavaScript that sends an asynchronous `Fetch` (AJAX) request to the Django endpoint `update-status/`. The request payload contains the card's unique prediction ID and its new status. The Django view updates the database record and returns a JSON response. Upon receiving a success status, JavaScript dynamically alters the HTML DOM, moving the card to the appropriate column with a CSS transition.

4. **Q: How is MySQL integrated with Django if Django defaults to SQLite?**
   * *A*: In `agri_portal/settings.py`, the `DATABASES` dictionary was modified to use `'ENGINE': 'django.db.backends.mysql'`. Because standard Python installations lack a native compiler to build the default `mysqlclient` on Windows, we installed `pymysql` and called `pymysql.install_as_MySQLdb()` in `agri_portal/__init__.py` to fake the MySQLdb connector interface.

---
This guide will ensure you present your project confidently and run it without any glitches! Good luck with your presentation!
