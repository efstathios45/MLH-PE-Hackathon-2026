import csv
from peewee import chunked
from app import create_app 
from app.database import db
from app.models.user import User
from app.models.url import Url
from app.models.event import Event

def load_users():
    with open("users.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    with db.atomic():
        for batch in chunked(rows, 100):
            User.insert_many(batch).on_conflict_ignore().execute()

def load_urls():
    # 1. Ask the database for a list of all VALID user IDs
    valid_users = set(str(u.id) for u in User.select(User.id))
    
    with open("urls.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        
    # 2. Filter out any URLs that belong to ghost/duplicate users
    clean_rows = [row for row in rows if row["user_id"] in valid_users]

    with db.atomic():
        for batch in chunked(clean_rows, 100):
            Url.insert_many(batch).on_conflict_ignore().execute()

def load_events():
    # 1. Ask the database for all VALID user IDs and url IDs
    valid_users = set(str(u.id) for u in User.select(User.id))
    valid_urls = set(str(u.id) for u in Url.select(Url.id))
    
    with open("events.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        
    # 2. Filter out bad events
    clean_rows = [
        row for row in rows 
        if row["user_id"] in valid_users and row["url_id"] in valid_urls
    ]

    with db.atomic():
        for batch in chunked(clean_rows, 100):
            Event.insert_many(batch).on_conflict_ignore().execute()

def setup():
    app = create_app()
    
    with app.app_context():
        print("Dropping old tables to start fresh...")
        db.drop_tables([Event, Url, User]) 
        
        print("Creating tables...")
        db.create_tables([User, Url, Event])
        
        print("Loading users...")
        load_users()
        
        print("Loading urls (skipping orphans)...")
        load_urls()
        
        print("Loading events (skipping orphans)...")
        load_events()
        
        print("Database seeded successfully! 🎉")

if __name__ == "__main__":
    setup()