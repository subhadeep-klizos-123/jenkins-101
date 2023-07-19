# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY main.py test-main.py /app/

# Install dependencies
RUN pip install pytest

# Set the command to run when the container starts
CMD ["pytest", "test-main.py"]
