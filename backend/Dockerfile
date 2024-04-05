# Use a base image with Python pre-installed
FROM python:latest

# Set working directory for backend
WORKDIR /app/backend

# Copy all Python files and requirements.txt into the container
COPY requirements.txt ./
COPY ./getData.py .


# Install dependencies from requirements.txt
RUN pip install --verbose --no-cache-dir -r requirements.txt

# Expose ports for each backend service
EXPOSE 5000 

# Add more EXPOSE directives for additional services if needed

# Command to run each backend service individually
CMD ["python", "getData.py"]