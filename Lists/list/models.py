from django.db import models

#2. implemant the database schema:
class List(models.Model):
    #what are the fields we need within the model:
    category = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

#create the second schema:
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    #which model does the item go into?:
    list_id = models.ForeignKey(List,on_delete=models.CASCADE)
    #make it human readable:
    def __str__(self):
        return self.name

#TODO: 2.make a function so the user can can create a category,
#1.make a form for the category function so it can be filled when created
# 3.create a template named board and within it is a link to create a category
#4.make each category a link that leads  to its own todo list
