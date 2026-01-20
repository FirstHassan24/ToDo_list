#import forms so django knows what your trying to do:
from django import forms
from .models import List,Item

#1.make a form for the category function so it can be filled when created

#create a form so the user can input data:
class ListForm(forms.ModelForm):
    #tell django which model to use and how to configure the form:
    class Meta:
        #asocciate this with your List model:
        model=List
        #make sure their fields match:
        fields=["category"]
