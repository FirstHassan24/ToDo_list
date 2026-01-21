from django.shortcuts import render,redirect
#import the models:
from .models import List,Item
#import the forms:
from .forms import ListForm
#import messages for error handling:
from django.contrib import messages
#2.make a function so the user can can create a category,link it to the listform:
def create_list(request):
    #check if the user clicked the link:
    if request.method =="POST":
        #fill the form with data the user inputs:
        form=ListForm(request.POST)
        #chech if the form fields are valid(non empy,correctly typed,etc):
        if form.is_valid():
                


