from django.db import models
# from django_mongodb_engine.contrib import MongoDBManager
# from djangotoolbox.fields import *

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=10, unique=True)
	# other = DictField()
	
	# objects = MongoDBManager()

	def __str__(self):
		return self.code

		