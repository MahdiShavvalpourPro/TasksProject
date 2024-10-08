# 1. استفاده از Python 3.9 به عنوان تصویر پایه
FROM python:3.11-slim

# 2. تنظیم دایرکتوری کاری در داخل کانتینر
WORKDIR /app

# 3. کپی کردن فایل‌های پروژه به دایرکتوری کاری
COPY . /app

# 4. نصب pip و وابستگی‌های پروژه از فایل requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. تنظیم دستور برای اجرای سرور Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
