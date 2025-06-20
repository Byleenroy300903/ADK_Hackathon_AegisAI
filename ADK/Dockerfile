# Use a slim Python 3.11 base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install OS dependencies
RUN apt-get update && \
    apt-get install -y git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy project files to the container
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install google-adk

# Optional: copy .env if you want it baked into the image
COPY .env /app/.env

# Expose the port your ADK app runs on
EXPOSE 8000

# Run the ADK web UI server
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]
