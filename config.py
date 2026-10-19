import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        print(f"Connection failed: {e}")
        raise e

if __name__ == "__main__":
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
        tables = cursor.fetchall()
        print("Connected successfully!")
        print("Tables:")
        for t in tables:
            print(f" - {t[0]}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")