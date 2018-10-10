from django.db import models

class Student(models.Model):
	roll=models.IntegerField()
	name=models.CharField(max_length=50)
	sub1_m=models.IntegerField()
	sub2_m=models.IntegerField()
	sub3_m=models.IntegerField()

def __str__(self):
    return self.name

