import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_failure(log_file):
    with open(log_file, "r", errors="ignore") as f:
        logs = f.read()

    prompt = f"""
You are an AI DevOps assistant.
Analyze the Jenkins pipeline logs and explain:
1. What failed
2. Why it failed
3. How to fix it

Logs:
{logs[:4000]}
"""

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    print("\n[MCP AI AGENT OUTPUT]\n")
    print(response.json()["response"])

if __name__ == "__main__":
    analyze_failure(sys.argv[1])
