----
## EVN Crawl Facebook
_____________
Dự án sử dụng các công cụ sau, để xử lý data cho người dùng
* Selenium
* Django Web API
* RPA

Dự án có thể áp dụng để quét data dạng lớn, đồng thời lưu trữ dữ liệu để phân tích data sau này

---------

Các tính năng chính:
 * Thu thập bình luận từ bài post (nội dung comment, người comment, link người comment)
 * Thu thập thông tin reaction từ bài post (thể loại reaction, số lượng reaction, )
 * Thu thập các bài post gần đây (đang phát triển)
 * Thu thập thông tin chung của bài post (đang phát triển)
 * 
---
Các tính năng phát triển tương lai:

* Phân tích mức độ tương tác của các thành viên
* Cảnh báo spam ở các bài post



___

| STT |                  Tính Năng                  | Ngày Hoàn Thành | Hướng Dẫn Sử Dụng |
|:---:|:-------------------------------------------:|:---------------:|:-----------------:|
|  1  |     Thu Thập Bình Luận Từ Một Bài Post      |   11/12/2022    |        N/A        |
|  2  | Thu Thập Thông Tin Reaction Từ Một Bài Post |   20/12/2022    |        N/A        |

---

1. Redis
2. Celery
Test celery: 
```bash
python manage.py shell
```
```bash
from EVNCrawlFacebookData.celery import debug_task
```
```bash
debug_task.delay()
```
```bash
celery -A proj worker -l INFO
```
