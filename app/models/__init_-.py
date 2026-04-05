from app.models.user import User
from app.models.url import Url
from app.models.event import Event

from flask import Flask
from app.database import db

# Import your new blueprint!
from app.routes.urls import urls_bp 

def create_app():
    app = Flask(__name__)
    
    # (Your database setup stuff is likely here)
    
    # Register the route!
    app.register_blueprint(urls_bp)
    
    return app