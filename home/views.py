from django.shortcuts import render
from .graph.plot_module import bar_plot, box_plot
import pandas as pd
from django.http import HttpResponseRedirect
from .forms import GetAPIRequestData
import pyrebase
from django.core.files.storage import default_storage

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
storage = firebase.storage()

#File upload 
def index(request):
    submitted = False
    if request.method == "POST":
        form = GetAPIRequestData(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv']
            fb_csv_file = default_storage.save(csv_file.name, csv_file)
            storage.child("files/" + csv_file.name).put(csv_file)
            npz_file = request.FILES['npz']
            fb_npz_file = default_storage.save(npz_file.name, npz_file)
            storage.child("files/" + npz_file.name).put(npz_file)
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

#Filter graph view
def graphs(request):
    box_plot_div = box_plot("sepal_width", "sepal_length", 'Apple Stocks')
    context = {
            'box_plot_div': box_plot_div
        }
    return render(request, 'graphs.html', context)
    
