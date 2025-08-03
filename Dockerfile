# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app code into container
COPY app/ .

# Expose port for FastAPI
EXPOSE 8000

# Start API using uvicorn
CMD ["python", "api.py"]
