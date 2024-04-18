# Use Docker Python image 
FROM python:3.9-slim-buster

# Set environment variables (For Avoid Creating .pyc files)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# Copy the rest of the directory
COPY . .

# Special command to run this
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
