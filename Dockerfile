FROM python:3.12-slim

# Set the environment variable for the time zone
ENV TZ=UTC

WORKDIR /TheServerBot

COPY requirements.txt /TheServerBot/

# Install necessary system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Set up a virtual environment
RUN python3 -m venv /venv

# Upgrade pip and install required Python packages
RUN /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt

# Copy the application code to the container
COPY . /TheServerBot/

# Update PATH environment variable to include the virtual environment binaries
ENV PATH="/venv/bin:$PATH"


# Command to run the application
CMD ["python", "main.py"]