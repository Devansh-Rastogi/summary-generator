from flask import Flask
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# MongoDB connection setup
MONGO_DETAILS = "mongodb://localhost:27017" 
client = MongoClient(MONGO_DETAILS)
database = client['bookRecommender']

# Collections
book_collection = database.get_collection("books")
review_collection = database.get_collection("reviews")
review_summary_collection = database.get_collection("reviewSummary")

# Import routes
from app import routes