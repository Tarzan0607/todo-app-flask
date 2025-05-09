# Stage 1: Build environment
FROM python:3.9-slim as builder

WORKDIR /app
# Install dependencies  
RUN pip install --no-cache-dir --prefix=/install flask

# Stage 2: Final minimal runtime environment
FROM python:3.9-slim

WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /install /usr/local

# Copy your app files into the container
COPY . /app

# Expose port 5000 for Flask
EXPOSE 3000

# Run the todo application
CMD ["python", "app.py"]
