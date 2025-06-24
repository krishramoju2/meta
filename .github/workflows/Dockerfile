FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    libnss3 \
    libatk1.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libgbm1 \
    libpangocairo-1.0-0 \
    libcups2 \
    libdrm2 \
    libxss1 \
    libxtst6 \
  && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN playwright install chromium

# Copy code
COPY insta_bot.py .

# Run the bot
CMD ["python", "insta_bot.py"]
