from flask import Flask
from app.database import init_db

def create_app():
    app = Flask(__name__)
    
    # 1. Initialize the Peewee database connection
    init_db(app)

    # 2. Import and Register Blueprints INSIDE the function to avoid circular loops
    from app.routes.urls import urls_bp
    app.register_blueprint(urls_bp)
    
    @app.route('/')
    def index():
        return "<h1>Database Connected!</h1><p><a href='/api/urls/'>View Data</a></p>"
    
    return app