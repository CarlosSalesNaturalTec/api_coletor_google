from firebase_admin import credentials, initialize_app, firestore
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    cred = credentials.Certificate(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
    initialize_app(cred)
    return firestore.client()
