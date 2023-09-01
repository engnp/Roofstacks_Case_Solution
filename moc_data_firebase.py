import firebase_admin
from firebase_admin import credentials, firestore
from faker import Faker
from datetime import datetime, timedelta
import pytz
import random

fake = Faker()

#cred = credentials.Certificate('test-63141-firebase-adminsdk-b94bj-1a31bf65f7.json')
cred = credentials.Certificate('/Users/engin/Downloads/test-63141-firebase-adminsdk-b94bj-1a31bf65f7.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def generate_users(count):
    users = []
    for _ in range(count):
        user = {
            "username": fake.user_name(),
            "email": fake.email(),
            #"createdAt": fake.date_time_between(start_date='-3m', end_date='now', tzinfo=pytz.UTC),
            #"modifiedAt": fake.date_time_between(start_date='-3m', end_date='now', tzinfo=pytz.UTC)
            "createdAt": fake.date_time_this_year(),
            "modifiedAt": fake.date_time_this_year()
        }
        users.append(user)
    return users

item_names = ["gold", "diamond", "ad-free", "beginner-bundle", "standard-bundle", "addicted-bundle", "ultimate-pack"]

def generate_items_for_user(user_id):
    items = []
    num_items = random.randint(0, 7)

    for _ in range(num_items):
        item_name = random.choice(item_names)
        item = {
            "userId": user_id,
            "itemName": item_name,
            ##"createdAt": fake.date_time_between(start_date='-3m', end_date='now', tzinfo=pytz.UTC),
            ##"modifiedAt": fake.date_time_between(start_date='-3m', end_date='now', tzinfo=pytz.UTC)
            "createdAt": fake.date_time_this_year(),
            "modifiedAt": fake.date_time_this_year()
        }
        items.append(item)
    return items

def insert_mock_data():
    users = generate_users(1000)

    for user in users:
        _, user_ref = db.collection('Users').add(user)
        user_id = user_ref.id
        items = generate_items_for_user(user_id)

        for item in items:
            db.collection('Items').add(item)

if __name__ == "__main__":
    insert_mock_data()