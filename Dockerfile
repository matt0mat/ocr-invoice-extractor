# Use an official lightweight Python image
FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
