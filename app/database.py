import os
from peewee import DatabaseProxy, Model, PostgresqlDatabase

# The proxy acts as a placeholder for the actual database
db = DatabaseProxy()

class BaseModel(Model):
    class Meta:
        database = db

def init_db(app):
    # Setup the actual connection settings
    database = PostgresqlDatabase(
        os.environ.get("DATABASE_NAME", "hackathon_db"),
        host=os.environ.get("DATABASE_HOST", "localhost"),
        port=int(os.environ.get("DATABASE_PORT", 5432)),
        user=os.environ.get("DATABASE_USER", "postgres"),
        password=os.environ.get("DATABASE_PASSWORD", "postgres"),
    )
    
    # Initialize the proxy with the real database
    db.initialize(database)

    @app.before_request
    def _db_connect():
        if db.is_closed():
            db.connect(reuse_if_open=True)

    @app.teardown_appcontext
    def _db_close(exc):
        if not db.is_closed():
            db.close()