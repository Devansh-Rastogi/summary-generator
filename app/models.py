from app import review_collection, review_summary_collection
from bson.objectid import ObjectId

def fetch_reviews_by_book_id(book_id: ObjectId):
    return review_collection.find({"bookId": book_id})

def create_review_summary(reviews):
    summary = " ".join([review["reviewText"] for review in reviews])
    return summary

def store_review_summary(book_id: str, summary: str):
    summary_data = {
        "book_id": book_id,
        "summary": summary
    }
    result = review_summary_collection.insert_one(summary_data)
    summary_data["_id"] = str(result.inserted_id)
    summary_data["book_id"] = str(book_id)
    summary_data["summary"] = str(summary)
    return summary_data
