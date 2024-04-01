import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage

# Use a service account.
cred = credentials.Certificate('firebase_credentials.json')
app = firebase_admin.initialize_app(cred)
storage_client = storage
bucket = storage_client.bucket('mmvae-e9218.appspot.com')

# List files in a specific folder
folder_name = 'files'
blobs = bucket.list_blobs(prefix=folder_name)
for blob in blobs:
  if blob.name.endswith('.txt'):
    print(blob.name)
    
# print string from a txt file
test_file = bucket.blob("files/test_file.txt").download_as_string()
print(test_file)