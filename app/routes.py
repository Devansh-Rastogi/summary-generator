from flask import jsonify, request
from bson.objectid import ObjectId
from app import app, review_collection, review_summary_collection
from .models import fetch_reviews_by_book_id, create_review_summary, store_review_summary
import traceback

@app.route("/summarize-reviews/<book_id>", methods=["POST"])
def summarize_reviews(book_id):
    try:
        print(book_id)
        reviews_cursor = fetch_reviews_by_book_id(book_id)
        print(reviews_cursor)
        # for x in reviews_cursor:
            # print(x)
        reviews = list(reviews_cursor)
        print(len(reviews))

        if not reviews:
            return jsonify({"error": f"No reviews found for book with ID {book_id}"}), 404

        # Create summary from reviews
        summary = create_review_summary(reviews)

        print(summary)

        # Store the summary in the database
        summary_data = store_review_summary(book_id, summary)

        return jsonify({"data": summary_data}), 201
    
    except Exception as e:
        return jsonify({"error": str(e.message)}), 500
