# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# Install any dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Install cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Add the cron job to execute the script every 5 minutes
RUN echo "*/5 * * * * python /app/main.py >> /app/cron.log 2>&1" > /etc/cron.d/script-cron

# Set the proper permissions for the cron file
RUN chmod 0644 /etc/cron.d/script-cron

# Apply the cron job
RUN crontab /etc/cron.d/script-cron

# Expose a log file to view the cron output
RUN touch /app/cron.log

# Run the cron daemon
CMD ["cron", "-f"]
