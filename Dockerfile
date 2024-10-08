FROM python:3.9-slim

# 2. تنظیم دایرکتوری کاری در داخل کانتینر
WORKDIR /app

# 3. کپی کردن فایل‌های پروژه به داخل کانتینر
COPY . /app

# 4. نصب وابستگی‌های پروژه (Django و دیگر بسته‌ها)
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 5. تنظیم دستور برای اجرای سرور Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
