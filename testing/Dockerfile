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

# Run the app
CMD ["cd app"]