from flask import Blueprint, jsonify
from app.models.url import Url
from playhouse.shortcuts import model_to_dict

# Define the blueprint with a prefix
urls_bp = Blueprint('urls', __name__, url_prefix='/api/urls')

@urls_bp.route('/', methods=['GET'])
def get_all_urls():
    # Fetch all records using the Url model
    urls = Url.select()
    
    # Convert Peewee objects to dictionaries for JSON response
    data = [model_to_dict(url) for url in urls]
    
    return jsonify(data)