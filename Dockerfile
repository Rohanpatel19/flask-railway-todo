FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Optional: expose for clarity (not required for Render)
EXPOSE 8000

# Run the app (we rely on app.py reading $PORT)
CMD ["python", "app.py"]
