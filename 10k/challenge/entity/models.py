from django.db import models
from django.conf import settings

class Entity(models.Model):

	symbol = models.CharField(max_length =200)
	CIK = models.CharField(max_length =200)

	row1 = models.CharField(max_length =500)
	row2 = models.CharField(max_length =500)
	row3 = models.CharField(max_length =500)


	def publish (self):
		self.save()

	def __str__(self):
		return self.name