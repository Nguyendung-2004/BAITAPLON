# 🏠 Homedy Crawler

Tự động thu thập dữ liệu bài đăng bất động sản từ [https://homedy.com](https://homedy.com), bao gồm:
- 🏷 Tiêu đề
- 📝 Mô tả
- 📍 Địa chỉ
- 📐 Diện tích
- 💰 Giá

Crawl dữ liệu **tất cả các trang** và lưu ra file Excel mỗi ngày lúc **6h sáng tự động**.

---

## 📦 Yêu cầu hệ thống

- Python 3.7 trở lên
- Google Chrome đã cài đặt
- ChromeDriver tương thích với Chrome
- Hệ điều hành: Windows / macOS / Linux

---

## 🔧 Cài đặt

### 1. Clone project
```bash
git clone https://github.com/your-username/homedy-crawler.git
cd homedy-crawler
```

### 2. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 3. Cài đặt ChromeDriver
- Vào: https://sites.google.com/chromium.org/driver/
- Tải đúng version với Chrome của bạn
- Đặt `chromedriver.exe` vào thư mục `chromedriver/` hoặc sửa đường dẫn trong script `crawl_homedy.py`

> 🔍 Kiểm tra version Chrome: mở trình duyệt → `chrome://settings/help`

---

## 📁 Cấu trúc thư mục

```
homedy-crawler/
├── crawl_homedy.py              # Script chính
├── requirements.txt             # Thư viện cần cài
├── README.md                    # Hướng dẫn
├── chromedriver/                # Nơi chứa ChromeDriver (nếu dùng)
└── homedy_data_YYYY-MM-DD.xlsx # File Excel lưu kết quả
```

---

## 🚀 Cách sử dụng

### ✅ Tự động crawl lúc 6h sáng mỗi ngày:

```bash
python crawl_homedy.py
```

> 📌 Script sẽ chạy nền, và đúng 6:00 sáng mỗi ngày sẽ tự crawl dữ liệu và lưu file Excel theo ngày (`homedy_data_2025-05-09.xlsx`...)

---

## ⚙️ Tuỳ chỉnh

### ➤ Thay đổi tỉnh/thành hoặc loại nhà đất

Mở file `crawl_homedy.py`, tìm dòng:

```python
url = "https://homedy.com/ban-can-ho-chung-cu-tp-ho-chi-minh"
```

Sau đó thay bằng URL phù hợp:

Ví dụ:
- Hà Nội – Căn hộ: `https://homedy.com/ban-can-ho-chung-cu-ha-noi`
- Đất Đà Nẵng: `https://homedy.com/ban-dat-da-nang`

---

## 🧪 Chạy thử ngay

Bạn có thể chạy script 1 lần để kiểm tra:

```bash
python crawl_homedy.py
```

Sau đó kiểm tra thư mục để thấy file `.xlsx` được tạo ra.

---

## 📌 Lưu ý

- Script dùng thư viện `schedule` để chạy tự động. Yêu cầu **máy luôn bật** (nếu không dùng cron hay Task Scheduler).
- Có thể mở rộng để gửi file Excel qua email, Google Drive hoặc đẩy lên GitHub.

---

## 📧 Liên hệ

Mọi thắc mắc, vui lòng tạo Issue hoặc liên hệ trực tiếp để được hỗ trợ.
