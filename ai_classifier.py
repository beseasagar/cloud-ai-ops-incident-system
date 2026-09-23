import requests
import json

def classify_issue(issue_text: str):
    prompt = f"""
    You are an AI Ops assistant. Classify the following issue into one category:
    - Performance
    - Network
    - Access
    - Configuration
    - Unknown

    Issue: {issue_text}

    Respond ONLY with the category name.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt},
        stream=True
    )

    full_output = ""

    # Read streaming JSON chunks line-by-line
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                chunk = data.get("response", "")
                full_output += chunk
            except json.JSONDecodeError:
                # Ignore malformed chunks
                continue

    return full_output.strip()
