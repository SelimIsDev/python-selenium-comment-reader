---

## 💬 Trendyol Comment Scraper (comment-reader.py)

This additional module is designed to extract user comments from product pages on the Trendyol website. It uses Python’s Selenium library to automate the scraping process and stores the retrieved data in an SQLite database.

---

### 🚀 Features

🛍 **Comment Extraction**  
- Automatically scrapes all visible user reviews from a given Trendyol product page.  
- Handles dynamic content loading and pagination using Selenium.  

💾 **Local Storage**  
- All extracted comments, including rating, date, and comment text, are saved into a local SQLite database.  
- Structured and searchable storage format.

⚙️ **Easy to Use**  
- The script is self-contained in `comment-reader.py`.  
- To use, simply **replace the sample URL** in the script with the Trendyol product link you want to scrape.

---

### ⚙️ How to Use

1. Install required dependencies:
   ```bash
   pip install selenium
