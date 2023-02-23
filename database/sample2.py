# Use firestore to query the database

import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

class User_DB:
    def __init__(self, username, password, attempt):
        self.username = username
        self.password = password
        self.attempt = attempt
    

    # Create
    def create(self):
        db.collection(u'users').document(self.username).set({
            u'password': self.password
        })
        return self

        
    # Read
    def read(self):
        doc_ref = db.collection(u'users').document(self.username)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
    # Update

    # Delete