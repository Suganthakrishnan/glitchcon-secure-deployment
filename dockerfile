# Use official Python image
FROM python:3.11-slim  

# Set the working directory
WORKDIR /app  

# Copy all files into the container
COPY . /app  

# Install Flask
RUN pip install flask  

# Run Flask when the container starts
CMD ["python", "app.py"]
