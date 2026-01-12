from django.db import models

#2. implemant the database schema:
class List(models.Model):
    #what are the fields we need within the model:
    name = models.CharField(max_length=100, unique=True)

#create the second schema:
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #which list does the item go into?:
    list_id = models.ForeignKey(List,on_delete=models.CASCADE)
    
