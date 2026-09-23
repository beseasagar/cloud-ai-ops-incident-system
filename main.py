from fastapi import FastAPI
from pydantic import BaseModel
from ai_classifier import classify_issue
from automation import perform_automation
from database import init_db, log_incident

app = FastAPI()

# Initialize database when API starts
init_db()

class Incident(BaseModel):
    issue: str

@app.post("/incident")
def receive_incident(incident: Incident):
    # Step 1: AI classification
    category = classify_issue(incident.issue)

    # Step 2: Automation
    action_result = perform_automation(category)

    # Step 3: Logging
    log_incident(incident.issue, category, action_result)

    return {
        "message": "Incident processed with AI, automation, and logging",
        "issue": incident.issue,
        "category": category,
        "automation_result": action_result
    }
