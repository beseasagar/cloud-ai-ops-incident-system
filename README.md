# Cloud + AI Ops Incident Processing System

A lightweight, local-first incident processing system that uses FastAPI, a local Llama 3 model (via Ollama), and Python automation scripts to classify and respond to operational issues. This project simulates how modern AI Ops platforms triage incidents, trigger automated actions, and maintain audit logs.

---

## Overview

This system does three things:

- Accepts incidents through a FastAPI endpoint
- Uses an AI model to classify the issue
- Runs an automated action based on the classification
- Logs everything into SQLite and a local log file

It is designed to be simple, modular, and easy to extend for real-world DevOps, SRE, or Cloud Engineering workflows.

---

## Features

- FastAPI endpoint for incident intake  
- Local AI classification using Llama 3 (Ollama)  
- Automation engine for predefined remediation actions  
- SQLite database logging  
- File-based logging for audit trails  
- Fully offline and free to run locally  
- Easy to extend with real automation scripts

---

## Architecture

┌──────────────────────────────────────────────────────────────┐
│                        Incident System                        │
└──────────────────────────────────────────────────────────────┘

User Request
     │
     ▼
┌──────────────┐       AI Classification       ┌──────────────┐
│   FastAPI     │  ─────────────────────────▶  │   Ollama      │
│  /incident    │                               │  Llama 3     │
└──────┬────────┘                               └──────┬───────┘
       │ category                                 category
       ▼                                          │
┌──────────────┐                                  ▼
│ Automation    │  ◀──────────────────────────────┘
│ Engine        │
└──────┬────────┘
       │ automation_result
       ▼
┌──────────────┐
│ Logging Layer │
│ SQLite + File │
└──────────────┘


---

## Use Cases

- Automatically classify incoming incidents  
- Trigger automated remediation actions  
- Build AI-driven triage workflows  
- Prototype AI Ops concepts locally  
- Maintain audit logs for analysis or dashboards  
- Extend into cloud-native automation (Azure, AWS, Kubernetes)

---

## API Details

### POST /incident

**Request Example**

{
"issue": "My server CPU is very high and everything is slow"
}


**Response Example**

{
"message": "Incident processed with AI, automation, and logging",
"issue": "My server CPU is very high and everything is slow",
"category": "Performance",
"automation_result": "Restarted service and cleared temporary files."
}


---

## File Structure

main.py            - FastAPI entry point
ai_classifier.py   - AI classification using Llama 3
automation.py      - Automated remediation logic
database.py        - SQLite logging functions
logger.py          - File logging setup
incidents.db       - SQLite database (auto-created)
incident.log       - File log (auto-created)


---

## Running the Project

### 1. Clone the repository

> git clone https://github.com/beseasagar/cloud-ai-ops-incident-system.git
> cd cloud-ai-ops-incident-system


### 2. Create a virtual environment

> python -m venv venv
> venv\Scripts\activate

### 3. Install dependencies

> pip install fastapi uvicorn requests

### 4. Start Ollama with Llama 3
> ollama run llama3

### 5. Start the API
> uvicorn main:app --reload

### 6. Open the API docs
> http://127.0.0.1:8000/docs

---

## Future Enhancements

- Add severity scoring  
- Add real automation (Docker, Kubernetes, Windows services)  
- Add Prometheus metrics and Grafana dashboards  
- Add multi-model classification  
- Add incident history visualization  
- Add cloud deployment (Azure Functions, AWS Lambda)  
- Add role-based access control  
- Add a UI dashboard (React or Streamlit)

---

## Why This Project Exists

Modern cloud systems generate thousands of incidents. AI Ops helps reduce manual triage, speed up remediation, and improve reliability. This project demonstrates how AI and automation can work together in a simple, understandable, and extendable way.

---

## License

MIT License
