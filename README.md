# Cloud + AI Ops Incident Processing System

A lightweight, local-first AI Ops project that uses **FastAPI, Python, Ollama, and Llama 3** to classify operational issues, trigger automated actions, and keep a record of what happened.

The idea is simple: **an incident comes in, AI figures out what it is, an appropriate action is triggered, and everything is logged.**

---

## Overview

This project demonstrates how AI and automation can work together to handle common operational incidents.

For example:

> **"My server CPU is very high and everything is slow."**

The system can:

* Receive the incident through an API
* Use Llama 3 to classify the issue
* Trigger a predefined automated action
* Store the result in SQLite
* Maintain a local log for tracking and auditing

It is intentionally lightweight and easy to extend for different **IT Operations, DevOps, SRE, and Cloud Engineering** scenarios.

---

## How It Works

```text
Incident
   ↓
FastAPI
   ↓
Llama 3 Classification
   ↓
Automation Action
   ↓
SQLite + Log
```

### Example

```text
"I can't access my account"
          ↓
       Access
          ↓
   Automated Action
          ↓
     Incident Logged
```

The current automation uses predefined actions, making the project easy to understand and modify.

---

## Features

* FastAPI incident intake
* Local AI classification using **Llama 3 + Ollama**
* Automated remediation logic
* SQLite incident database
* File-based audit logging
* Fully local and free to run
* Simple and modular structure
* Easy to extend with additional automation

---

## Architecture

```text
                    ┌──────────────┐
                    │   FastAPI    │
                    │   /incident  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │    Ollama    │
                    │    Llama 3   │
                    └──────┬───────┘
                           │
                      Classification
                           │
                           ▼
                    ┌──────────────┐
                    │  Automation  │
                    │    Engine    │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ SQLite + Log │
                    └──────────────┘
```

---

## Example API

### POST `/incident`

**Request**

```json
{
  "issue": "My server CPU is very high and everything is slow"
}
```

**Response**

```json
{
  "message": "Incident processed with AI, automation, and logging",
  "issue": "My server CPU is very high and everything is slow",
  "category": "Performance",
  "automation_result": "Restarted service and cleared temporary files."
}
```

---

## Project Structure

```text
main.py              → FastAPI application
ai_classifier.py     → Llama 3 classification
automation.py        → Automated actions
database.py          → SQLite logging
logger.py            → File logging
incidents.db         → Incident database
incident.log         → Activity log
```

---

## Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/beseasagar/cloud-ai-ops-incident-system.git
cd cloud-ai-ops-incident-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn requests
```

### 4. Start Llama 3 with Ollama

```bash
ollama run llama3
```

### 5. Start the API

```bash
uvicorn main:app --reload
```

### 6. Open the API documentation

```text
http://127.0.0.1:8000/docs
```

---

## Use Cases

The project can be adapted for different operational environments, such as:

* IT support
* DevOps
* Cloud operations
* Network operations
* SRE workflows
* Service desk automation
* Application support

The same concept could also be adapted to other organizations and service environments where repetitive operational issues need to be classified, processed, and tracked.

---

## Future Enhancements

* Severity and priority scoring
* Prometheus and Grafana monitoring
* Incident history dashboard
* More automated remediation actions
* Docker and Kubernetes integration
* Azure or AWS deployment
* Web-based UI
* Role-based access control
* Additional AI models

---

## Why This Project?

Modern IT environments generate many small incidents that require repetitive triage and response.

This project explores a simple approach to combining **AI + automation + logging** so that routine operational issues can be processed more efficiently while maintaining visibility into what the system did.

---

## License

MIT License
