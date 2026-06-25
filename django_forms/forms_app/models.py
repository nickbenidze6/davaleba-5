from django.db import models
 
class Student(models.Model):
    firstname = models.CharField()
    lastname = models.CharField()
    age = models.CharField()
    course = models.CharField()

    def __str__(self):
        return self.firstname
    
class Book(models.Model):
    title = models.CharField()
    author = models.CharField()
    writed_at = models.DateField()

    def __str__(self):
        return self.title
