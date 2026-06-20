# 🏁 AgriGrow - Local Run & Expose Guide

Follow these step-by-step procedures to restart and run your Django server and expose it securely to the internet after restarting your PC.

---

## 🚀 Step 1: Run the Django Web Server
1. Open **Command Prompt** (cmd) on your PC.
2. Navigate to your project directory:
   ```cmd
   E:
   cd "E:\INTERN PROJECT\project"
   ```
3. Activate the virtual environment:
   ```cmd
   .venv\Scripts\activate
   ```
4. Start the Django development server:
   ```cmd
   python manage.py runserver 8000
   ```
   *(Keep this terminal window open!)*

---

## 🌐 Step 2: Generate a Public Internet Link (SSH Tunnel)
Because your local server runs at `http://127.0.0.1:8000/`, it is only visible on your machine. To make it visible on the internet for free without hosting, open a **second** Command Prompt window and run:

```cmd
ssh -o StrictHostKeyChecking=no -R 80:localhost:8000 nokey@localhost.run
```

Once connected, look for the line in the terminal that says:
`https://xxxxxxx.lhr.life tunneled with tls termination`

Copy that URL (e.g., `https://1a0e9701fc7c63.lhr.life`) and open it in your browser or share it.

---

## 🛡️ Admin Panel Credentials
Access the admin portal at `<your-live-url>/admin/` using:
- **Username**: `admin`
- **Password**: `adminpassword`

---

## ☁️ Continuous Vercel Cloud Deployment
If you prefer running on Vercel with your Supabase database:
1. Ensure your latest changes are pushed to GitHub:
   ```cmd
   git push -u origin main --force
   ```
2. Your website will be automatically updated and permanently hosted at:
   **https://agri-crow-smart-agriculture-predict.vercel.app/**
