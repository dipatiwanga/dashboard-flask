import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application configuration
APP_NAME = os.getenv('APP_NAME', 'BI Dashboard')
BASE_URL = os.getenv('BASE_URL', '/')

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'db')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME', 'bi_dashboard')
DB_USER = os.getenv('DB_USER', 'bi_user')
DB_PASS = os.getenv('DB_PASS', 'bi_password')

# Timezone
TIMEZONE = 'Asia/Jakarta'
