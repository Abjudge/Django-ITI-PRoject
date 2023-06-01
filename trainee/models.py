from django.db import models
from course.models import *

class Traineee (models.Model):
    id= models.AutoField(primary_key=True)
    name= models.TextField()
    courseid=models.ForeignKey("course.Course",on_delete=models.CASCADE)