from SQLSave import SetData
from selenium import webdriver
import time
from bs4 import BeautifulSoup

comments_data = SetData()

url = 'https://www.trendyol.com/umtlifes/kadin-siyah-ici-peluslu-kislik-termal-tayt-p-364743241/yorumlar?boutiqueId=61&merchantId=532623&v=s'

driver = webdriver.Chrome()
driver.get(url)

count = 0
current_scroll_position = 0
scroll_step = 1000
seen_comments = set()
stars_count = 0

while True:
    current_scroll_position += scroll_step
    driver.execute_script(f"window.scrollTo(0, {current_scroll_position});")
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    comments = soup.find_all('div', {"class": "comment"})

    for comment in comments:
        real_comments = comment.find_all('div', {"class": "comment-text"})
        stars_container = comment.find_all('div', {"class": "full"})
        
        stars_string = "\n".join(str(item) for item in stars_container)

        stars1 = stars_string.count('"width: 0%')
        stars2 = stars_string.count('"width: 0px')

        stars_all = stars1 + stars2
        stars_count = 5 - stars_all
        
        target_text1 = '"width: 0%;'
        target_text2 = '"width: 0px;'

        
        for real_comment in real_comments:
            text = real_comment.text.strip()
            if text not in seen_comments:
                count += 1
                seen_comments.add(text)
                print(f"Yorum {count}: {text}")
                print(f"Yıldız Sayısı: {stars_count}\n")
                comments_data.add_comment(text, stars_count)


print(count + "Yorum ve Puan Kaydedildi...")

driver.quit()
