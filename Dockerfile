# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Ensure environment variables are set
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run database migrations
RUN flask db upgrade

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
