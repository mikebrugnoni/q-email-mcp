#!/usr/bin/env python3
import json
import requests

# MCP server endpoint
url = "http://localhost:8080/mcp/v1/invoke"

# Request payload
payload = {
    "name": "setup_oauth",
    "parameters": {
        "credentials_path": "/home/mbrug/repos/mcp/certificate.json"
    }
}

# Make the request
response = requests.post(url, json=payload)
print(f"Status code: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")
