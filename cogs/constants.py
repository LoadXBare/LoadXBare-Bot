from datetime import datetime
from dotenv import load_dotenv
import os
import psycopg2 as psycopg2

load_dotenv()

start_time = datetime.utcnow()
database = psycopg2.connect(
    database=os.getenv('DB_DATABASE'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port='5432'
)
is_bot = ['<@819664773146345503>', '<@!819664773146345503>']
