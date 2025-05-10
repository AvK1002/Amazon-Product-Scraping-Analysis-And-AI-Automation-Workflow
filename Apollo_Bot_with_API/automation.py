import requests
import os
import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("APOLLO_API_KEY")

def search_apollo_person(name_query, company_domain=None):
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "X-Api-Key": API_KEY
    }

    url = "https://api.apollo.io/v1/people/match"
    payload = {
        "name": name_query,
        "enrich_profiles": "true"  # Request enriched data if available
    }
    
    if company_domain:
        payload["company_domain"] = company_domain

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        
        data = response.json()
        if not data.get("person"):
            return {"error": "No person found in response"}
            
        person = data["person"]
        
        # Handle organization data more robustly
        company = "N/A"
        org = person.get("organization") or person.get("current_employment") or {}
        if isinstance(org, dict):
            company = org.get("name") or org.get("company") or org.get("company_name") or "N/A"
        elif isinstance(org, str):
            company = org
            
        # Get first available email
        email = person.get("email") 
        if not email and person.get("email_status") == "verified":
            email = person.get("sanitized_email") or person.get("email_address")
            
        return {
            "name": person.get("name", "N/A"),
            "title": person.get("title") or person.get("headline") or "N/A",
            "company": company,
            "email": email or "N/A",
            "linkedin": person.get("linkedin_url") or person.get("linkedin") or "N/A",
            "raw_response": person  # Include for debugging
        }
        
    except Exception as e:
        return {"error": f"API request failed: {str(e)}"}
    
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