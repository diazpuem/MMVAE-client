# import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('mmvae-e9218-firebase-adminsdk-puokr-c7d6d8f37e.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# config = {
#   'apiKey': "AIzaSyBla8oQsWu2U7_AtXSWsMvdDkMu6DZ9aXs",
#   'authDomain': "mmvae-e9218.firebaseapp.com",
#   'projectId': "mmvae-e9218",
#   'storageBucket': "mmvae-e9218.appspot.com",
#   'messagingSenderId': "221017647575",
#   'appId': "1:221017647575:web:f1c47d2c261bb54c838392",
#   'measurementId': "G-YNB3HV8GKW",
#   'databaseURL': "",
#   'serviceAccount': "mmvae-e9218-firebase-adminsdk-puokr-c7d6d8f37e.json"
# }

# firebase = pyrebase.initialize_app(config)
# storage = firebase.storage()

# path = "data"

# ref = db.reference("files")
# ab=str(1)    
# all_files = storage.child("files").list_files()
users_ref = db.collection("files")
all_files = users_ref.stream()

print(all_files)
cnt = 0
for file in all_files:
  print(f"{file.id} => {file.to_dict()}")
  cnt += 1