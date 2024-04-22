from django.shortcuts import render
from .graph.plot_module import box_plot
import pandas as pd
from django.http import HttpResponseRedirect
from .forms import GetAPIRequestData
import pyrebase
from django.core.files.storage import default_storage
import firebase_admin
from firebase_admin import credentials, storage

config = {
  'apiKey': "AIzaSyBla8oQsWu2U7_AtXSWsMvdDkMu6DZ9aXs",
  'authDomain': "mmvae-e9218.firebaseapp.com",
  'projectId': "mmvae-e9218",
  'storageBucket': "mmvae-e9218.appspot.com",
  'messagingSenderId': "221017647575",
  'appId': "1:221017647575:web:f1c47d2c261bb54c838392",
  'measurementId': "G-YNB3HV8GKW",
  'databaseURL': ""
}

# // Initialize Firebase
firebase = pyrebase.initialize_app(config)
firebase_storage = firebase.storage()

# // Initialize Admin Storage
output_file_name = "output_test.txt"
input_file_name = "input.csv"

# Use a service account.
cred = credentials.Certificate('./firebase_credentials.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'mmvae-e9218.appspot.com'
})
bucket = storage.bucket()


#File upload 
def index(request):
    submitted = False
    if request.method == "POST":
        form = GetAPIRequestData(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv']
            fb_csv_file = default_storage.save(csv_file.name, csv_file)
            firebase_storage.child("files/" + csv_file.name).put(csv_file)
            npz_file = request.FILES['npz']
            fb_npz_file = default_storage.save(npz_file.name, npz_file)
            firebase_storage.child("files/" + npz_file.name).put(npz_file)
            delete_csv = default_storage.delete(csv_file.name)
            delete_npz = default_storage.delete(npz_file.name)

            form.save()
            
            return HttpResponseRedirect('/index?submitted=True')
        else:
            print(form.errors)
    else:
        form = GetAPIRequestData()
        if 'submitted' in request.GET:
            submitted = True
            
    context = {
        'submitted': submitted,
        'form': form,
    }
    return render(request, 'index.html', context)

def results(request):
    bucket = storage.bucket()
    blobs = bucket.list_blobs()
    for blob in blobs:
        if str(blob.name) == "files/" + input_file_name:
            input_last_updated = blob.updated
        if str(blob.name) == "files/" + output_file_name:
            output_last_updated = blob.updated
    
    
    if input_last_updated and output_last_updated:
        if output_last_updated > input_last_updated:
            output_file_text = bucket.blob("files/output_test.txt").download_as_string()
            message = output_file_text
        else:
            message = "No new submission"
    else:
        message = "Error receiving dates"
        
    context = {
            'message' : message
    }
    return render(request, 'results.html', context)

#Filter graph view
def graphs(request):
    box_plot_div = box_plot("sepal_width", "sepal_length", 'Apple Stocks')
    context = {
            'box_plot_div': box_plot_div
        }
    return render(request, 'graphs.html', context)
    
