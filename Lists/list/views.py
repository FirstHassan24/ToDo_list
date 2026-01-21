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
            #save it to the DB:
            form.save()
            #after creating send the user back to the board:
            return redirect("board")
    #if the user is just visiting the page return an empty form:
    else:
        form=ListForm()
        #render the form  inside the form template
        #TODO: create a List_form.html template
        #CReat a function that displays the categorys in the main page:
        def board(request):
            #store all the models in a variable:
            categorys = List.objects.all()
            items = Item.objects.all()
            #TODO:create a bord.html template and then render this view their:





