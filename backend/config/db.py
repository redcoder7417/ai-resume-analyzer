from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["ai_resume_analyzer"]

users_collection = db["users"]
chats_collection = db["chats"]
resumes_collection = db["resumes"]