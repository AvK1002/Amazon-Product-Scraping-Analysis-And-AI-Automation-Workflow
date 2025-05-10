import requests
import os
import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("APOLLO_API_KEY")
print(f"Loaded API Key: {API_KEY}")

def search_apollo_person(name_query):
    headers = {
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    params = {
        "q_organization_domains": "",
        "person_names": name_query,
        "page": 1,
        "per_page": 1
    }

    # ✅ Using dummy local API
    url = "http://127.0.0.1:5000/v1/mixed_people/search"

    # For dummy API, use GET or POST depending on your dummy server setup
    response = requests.post(url, headers=headers, json=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("people"):
            person = data["people"][0]  # Top result
            return {
                "name": person.get("name", "N/A"),
                "title": person.get("title", "N/A"),
                "company": person.get("organization", {}).get("name", "N/A"),
                "email": person.get("email", "N/A"),
                "linkedin": person.get("linkedin_url", "N/A")
            }
        else:
            return {"error": "No results found"}
    else:
        return {"error": f"API error: {response.status_code}"}

def log_to_sheet(prompt, results):
    # Define the scopes
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # Load credentials
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    # Open your Google Sheet (ensure service account email has access)
    sheet = client.open("Apollo Lookup Logs").sheet1

    # Prepare row data
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = results.get("name", "N/A")
    email = results.get("email", "N/A")
    company = results.get("company", "N/A")
    title = results.get("title", "N/A")
    linkedin = results.get("linkedin", "N/A")

    # Append the data
    sheet.append_row([now, prompt, name, title, company, email, linkedin])
