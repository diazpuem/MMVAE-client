from firebase_admin import credentials, storage
import firebase
import datetime
import os

# Use a service account.
cred = credentials.Certificate('firebase_credentials.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'mmvae-e9218.appspot.com'
})
bucket = storage.bucket()

# List files in a specific folder
folder_name = "files"
blobs = bucket.list_blobs()

# Name of files
input_file_name = "input.csv"
output_file_name = "output_test.txt"

# for blob in blobs:
#     if blob.name == input_file_name:
#         input_file_blob = blob
#         print(input_file_blob)
#     elif blob.name == output_file_name:
#         output_file_blob = blob

# input_last_updated = get_file_last_updated(f"files/{input_file_name}", blobs)
# print(str(input_last_updated))
# output_last_updated = get_file_last_updated(f"files/{output_file_name}", blobs)
# input_last_updated = ""
# output_last_updated = ""

for blob in blobs:
      print(str(blob.name))
      if str(blob.name) == "files/{input_file_name}":
        # Retrieve the metadata of the blob to get the last updated timestamp
        input_last_updated = blob.updated
        print(input_last_updated)
      if str(blob.name) == "files/{output_file_name}":
        output_last_updated = blob.updated
        print(output_last_updated)
  
if input_last_updated and output_last_updated:
    if output_last_updated < input_last_updated:
        # Define the file to upload and its contents
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Current date and time
        content = "Uploaded at: " + current_time

        # Upload content to Firebase Storage
        new_blob = bucket.blob(f"files/{output_file_name}")
        new_blob.upload_from_string(content)
        
        print(f"File uploaded successfully: {new_blob.name}")
      
    else:
        print("No new submission")
else:
    print("Error receiving dates")
