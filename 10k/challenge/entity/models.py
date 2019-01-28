from django.db import models
from django.conf import settings

class Entity(models.Model):

	symbol = models.CharField(max_length =200)
	CIK = models.CharField(max_length =200)

	payload = models.TextField()


	def publish (self):
		self.save()

	def __str__(self):
		return self.symbol