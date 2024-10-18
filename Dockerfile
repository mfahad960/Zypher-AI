# Use the official Python base image
FROM python:3.11-slim

# Set environment variables to avoid Python writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
# Set environment variables to ensure Python outputs everything to the console
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/

# Install the necessary Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port the app will run on (8080 as per your configuration)
EXPOSE 8080

# Set the command to run the Flask app
CMD ["python", "app.py"]
