from automation import search_apollo_person, log_to_sheet

if __name__ == "__main__":
    query = input("Enter the person you want to search: ")
    result = search_apollo_person(query)
    log_to_sheet(query, result)
    print("Result logged to Google Sheet.")
    print(result)
