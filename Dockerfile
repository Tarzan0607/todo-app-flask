# Use official Python image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy project files to container
COPY . /app

# Install dependencies
RUN pip install flask

# Ensure the data directory exists 
RUN mkdir -p /data

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
