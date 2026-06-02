# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Render uses
EXPOSE 10000

# Start the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
