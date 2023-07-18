from django.db import models

class Person(models.Model):
    Parent_name = models.CharField(max_length=100)
    Parent_key = models.CharField(max_length=100)
    children_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100 )
    date = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return "Name : "+self.name +" "+"Age : "+str(self.age)