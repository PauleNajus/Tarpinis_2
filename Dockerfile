# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure environment variables are set
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV ADMIN_USERNAME=admin
ENV ADMIN_EMAIL=admin@admin.com
ENV ADMIN_PASSWORD=admin123

RUN flask db upgrade
RUN python -c "from app import init_admin_user; init_admin_user()"

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
