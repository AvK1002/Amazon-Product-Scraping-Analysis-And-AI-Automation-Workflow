# Amazon-Product-Scraping-Analysis-And-AI-Automation-Workflow

# 🧸 Amazon Soft Toys Sponsored Products Scraper & Analysis

## 📌 Project Overview

This project focuses on scraping *sponsored product listings* for the keyword **"soft toys"** from [Amazon.in](https://www.amazon.in) using **Selenium** and **BeautifulSoup**, followed by **data cleaning**, **analysis**, and **visualization** using **pandas**, **matplotlib**, and **seaborn**.

---

## 🚀 Features

* Scrapes sponsored listings only
* Extracts product title, brand, price, rating, reviews, image URL, and product URL
* Cleans and processes data (e.g., ₹999 → 999, 1,234 → 1234)
* Generates visualizations:

  * Top 5 Brands by Frequency
  * Brand Share (Pie Chart)
  * Price vs. Rating (Scatter)
  * Avg Price by Rating Range
  * Top Products by Reviews and Ratings
* Saves cleaned data and plots for reporting

---

## 🛠️ Tools & Libraries

* Python 3.x
* Selenium
* BeautifulSoup
* pandas
* matplotlib
* seaborn
* ChromeDriver (via `webdriver-manager`)

---

## 📂 Project Structure

```
amazon_soft_toys/
├── amazon_analysis/
│   ├── brand_frequency.png
│   ├── brand_share_pie.png
│   ├── price_vs_rating.png
│   ├── avg_price_rating.png
│   ├── top_reviews.png
│   ├── top_ratings.png
│   └── soft_toys_sponsored_cleaned.csv
├── soft_toys_scraper_analysis.py
```

---

## ✅ How to Run

1. Install requirements:

   ```
   pip install -r requirements.txt
   ```
2. Run the script:

   ```
   python soft_toys_scraper_analysis.py
   ```
3. Outputs will be saved in the `amazon_analysis/` folder.

---






# 🚀 Apollo People Lookup Automation
This project is part of the AI Automation Internship Assignment – 

Task 1. It automates the process of finding professional details about people using the Apollo.io People Lookup API and logs the results into a Google Sheet.

## 📌 Features
🔎 Person Search: Input any person’s name and retrieve their details (Name, Title, Company, Email, LinkedIn).

🧠 Apollo API Integration: Connects to the Apollo API to fetch verified professional data.

📄 Logging: Automatically saves search queries and results to a Google Sheet.

✅ .env Support: Securely manages API keys using environment variables.

✅ Mock API Support: Can use a dummy local API for testing purposes.

## 🛠️ Technologies Used
Python 3

requests – for making HTTP calls

gspread – for interacting with Google Sheets

oauth2client – for Google API credentials

dotenv – for loading environment variables

Flask (optional, for mock API testing)

## 🧪 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/apollo-lookup-automation.git
cd apollo-lookup-automation
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Add .env File
Create a .env file in the project root with your Apollo API key:

env
Copy
Edit
APOLLO_API_KEY=your_actual_apollo_api_key
4. Set Up Google Sheets
Create a Google Sheet named Apollo Lookup Logs

Share it with the email from your creds.json service account

Save the creds.json file in the root of the project

5. Run the Script
bash
Copy
Edit
python main.py
## ✅ Example Output
bash
Copy
Edit
Enter the person you want to search: Sundar Pichai
Result logged to Google Sheet.
{
  'name': 'Sundar Pichai',
  'title': 'CEO',
  'company': 'Google',
  'email': 'sundar@google.com',
  'linkedin': 'https://linkedin.com/in/sundarpichai'
}
## 🧪 Testing with Mock API (Optional)
If Apollo API is not accessible, you can test using a local Flask dummy API:

bash
Copy
Edit
python mock_api.py
Then update the search URL in automation.py:

python
Copy
Edit
url = "http://127.0.0.1:5000/v1/mixed_people/search"
📁 Files Overview
main.py: Runs the input + search + log pipeline

automation.py: Contains the core functions

mock_api.py: A dummy API for local testing

creds.json: Google Sheets service account credentials

.env: Contains your Apollo API key


# 🔐 API Security (Secret Key)

This project uses a **secret key** to secure access to the API. To run the application successfully, you need to provide this key.

#### Setting the Secret Key

1. **Create a `.env` file** in the root directory of the project (if not already present).

2. Add the following line to the `.env` file:

   ```bash
   SECRET_KEY=your_secret_key_here
   ```

3. Ensure your application loads the secret key from environment variables (e.g., using `os.environ.get('SECRET_KEY')` in Python).

#### Important Notes

* **Do not** share your secret key publicly.
* The `.env` file is listed in `.gitignore` and should never be committed to version control.
* For production environments, set the `SECRET_KEY` securely using environment-specific configuration.

---

## 📌 Note
Ensure your Apollo API key is valid and active.

If 401 Unauthorized errors occur, verify your API key in .env.

## 📌 Notes

* Amazon often changes HTML structure — this scraper may need updates in the future.
* Headless Chrome is used for fast scraping.


## 🧑‍💻 Author

Maintained by Aswin V Kumar

