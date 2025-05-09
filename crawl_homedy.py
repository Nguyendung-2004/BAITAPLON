from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import schedule
import time
import datetime

# === CẤU HÌNH TRÌNH DUYỆT ===
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    service = Service("PATH_TO_CHROMEDRIVER") 
    return webdriver.Chrome(service=service, options=chrome_options)

# === HÀM CRAWL ===
def crawl_homedy():
    print(f"Đang chạy crawl lúc {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    driver = get_driver()
    url = "https://homedy.com/ban-can-ho-chung-cu-tp-ho-chi-minh" 
    driver.get(url)
    time.sleep(3)

    data = []

    def extract_info(post_element):
        try:
            title = post_element.find_element(By.CLASS_NAME, "title").text.strip()
        except: title = ''
        try:
            description = post_element.find_element(By.CLASS_NAME, "post-summary").text.strip()
        except: description = ''
        try:
            address = post_element.find_element(By.CLASS_NAME, "post-location").text.strip()
        except: address = ''
        try:
            area = post_element.find_element(By.CLASS_NAME, "post-acreage").text.strip()
        except: area = ''
        try:
            price = post_element.find_element(By.CLASS_NAME, "post-price").text.strip()
        except: price = ''
        return {
            "Tiêu đề": title,
            "Mô tả": description,
            "Địa chỉ": address,
            "Diện tích": area,
            "Giá": price
        }

    while True:
        time.sleep(2)
        posts = driver.find_elements(By.CLASS_NAME, "property-item")
        for post in posts:
            data.append(extract_info(post))
        # Trang tiếp theo
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, ".pagination .page-item.next a")
            driver.execute_script("arguments[0].click();", next_btn)
        except:
            break

    df = pd.DataFrame(data)
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    df.to_excel(f"homedy_data_{today}.xlsx", index=False)
    print(f"Đã lưu file: homedy_data_{today}.xlsx")
    driver.quit()

# === LỊCH CHẠY ===
schedule.every().day.at("06:00").do(crawl_homedy)

print("Đang chờ đến 6h sáng mỗi ngày để crawl...")
while True:
    schedule.run_pending()
    time.sleep(60)
