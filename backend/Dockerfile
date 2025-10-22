# Use the official Python 3 image
FROM python:3.13

# Set Working Directory
WORKDIR /app/

# Set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . ./app/app

EXPOSE 8000

# Run the app
CMD ["cd app"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]