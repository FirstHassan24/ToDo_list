from django.shortcuts import render,redirect,get_object_404
#import the models:
from .models import List,Item
#import messages for error handling:
from django.contrib import messages

# Create your views here.
#1. make a view where a user can create a list:
def create_list(request):
    
