import mysql.connector
from mysql.connector import Error
import config
import os

def get_db_connection():
    """
    Create and return a MySQL database connection.
    Reads configuration from config.py (which loads from environment variables).
    """
    try:
        connection = mysql.connector.connect(
            host=config.DB_HOST,
            port=config.DB_PORT,
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASS,
            charset='utf8mb4',
            autocommit=True
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        # For testing without database, return None instead of raising
        return None
