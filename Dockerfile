# Use official lightweight Python image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Expose Flask default port
EXPOSE 8000

# Command to run Flask app
CMD ["python", "app.py"]
