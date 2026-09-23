🌐 Cloud + AI Ops Incident Processing System
A lightweight, local-first AI Ops automation system built using FastAPI, Ollama (Llama 3), SQLite, and Python automation scripts.
This project simulates real-world cloud operational workflows:

Incident intake

AI-powered classification

Automated remediation

Operational logging

Full API documentation

Perfect for showcasing cloud, AI, automation, and backend engineering skills.

🚀 Features
Incident Intake API using FastAPI

AI Classification using Llama 3 (local model via Ollama)

Automated Remediation based on incident category

SQLite Logging for persistent history

File Logging for operational audit trails

Modular Architecture (easy to extend)

Fully local, free, and offline

🧠 Architecture Overview
User → FastAPI API → AI Classifier (Ollama) → Automation Engine → Logging (SQLite + File)

Components
File	Purpose
main.py	API entry point
ai_classifier.py	AI Ops classification using Llama 3
automation.py	Automated remediation actions
database.py	SQLite logging engine
logger.py	File-based logging

📡 API Endpoint
POST /incident
Request

{
  "issue": "My server CPU is very high and everything is slow"
}

Response

{
  "message": "Incident processed with AI, automation, and logging",
  "issue": "My server CPU is very high and everything is slow",
  "category": "Performance",
  "automation_result": "Restarted service and cleared temporary files."
}

🛠️ Tech Stack
Python 3
FastAPI
Uvicorn
Ollama (Llama 3)
SQLite
VS Code
Git + GitHub

▶️ Run Locally
1. Clone the repo

> git clone https://github.com/beseasagar/cloud-ai-ops-incident-system.git
> cd cloud-ai-ops-incident-system

2. Create virtual environment

> python -m venv venv
> venv\Scripts\activate

3. Install dependencies

> pip install fastapi uvicorn requests

4. Start Ollama

> ollama run llama3

5. Start API

> uvicorn main:app --reload

6. Open API docs

> http://127.0.0.1:8000/docs

🔮 Future Enhancements

Add Prometheus/Grafana monitoring
Add real automation (restart Docker, clear logs, scale services)
Add multi-model AI classification
Add incident severity scoring
Add email/SMS notifications
Add dashboard UI (React or Streamlit)

📘 Why This Project Matters

This project demonstrates:

AI-driven decision making
Cloud operations automation
Backend API development
Logging and observability
Real-world incident management workflows