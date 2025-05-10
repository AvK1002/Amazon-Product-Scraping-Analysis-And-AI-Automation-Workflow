from automation import search_apollo_person, log_to_sheet
from datetime import datetime

def display_results(result):
    """Display results in a user-friendly format"""
    print("\n=== Search Results ===")
    if "error" in result:
        print(f"Error: {result['error']}")
        return
    
    for key, value in result.items():
        if key not in ["error", "raw_response"]:  # Skip technical fields
            print(f"{key.title():<10}: {value or 'Not available'}")

def main():
    print("Apollo Person Search")
    print("-------------------")
    
    name_query = input("Enter the person's name: ").strip()
    if not name_query:
        print("Error: Name cannot be empty")
        return
    
    # Optional: Add company domain for better results
    company_domain = input("Optional - Enter company domain (e.g., google.com): ").strip()
    
    print("\nSearching...")
    search_start = datetime.now()
    
    # Fetch the person data
    result = search_apollo_person(
        name_query,
        company_domain=company_domain if company_domain else None
    )
    
    # Calculate search duration
    search_duration = (datetime.now() - search_start).total_seconds()
    
    # Display results
    display_results(result)
    print(f"\nSearch completed in {search_duration:.2f} seconds")
    
    # Log the result to Google Sheets if successful
    if "error" not in result:
        try:
            log_to_sheet(name_query, result)
            print("Results logged to Google Sheets")
        except Exception as e:
            print(f"Warning: Could not log to Google Sheets - {str(e)}")

if __name__ == "__main__":
    main()