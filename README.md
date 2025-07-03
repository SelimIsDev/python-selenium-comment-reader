---

## 💬 Trendyol Comment Scraper (comment-reader.py) | 2023

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

2. Make sure ChromeDriver is installed and available in your PATH.
3. Open comment-reader.py and replace the url variable:
   ```python
   url = "https://www.trendyol.com/some-product-link"
4. Run the comment-reader.py

### 🖼️ Screenshots
<img src='https://github.com/user-attachments/assets/fb1786fc-ae2c-4397-8db3-a46933ebe371' width='400'>
<img src='https://github.com/user-attachments/assets/721fd619-62c7-4536-86fb-e7ca36b22017' width='300' height='220'>

