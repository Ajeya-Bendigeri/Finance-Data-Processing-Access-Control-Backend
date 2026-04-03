from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

def init_db():
    connect(
        db=os.getenv("db_name"),
        host=os.getenv("db_host"),
        port=int(os.getenv("db_port"))
    )
    print("MongoDB Connected")