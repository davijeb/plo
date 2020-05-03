from django.db import models


class User(models.Model):

	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	phone = models.CharField(max_length=200) 
	country = models.CharField(max_length=100)
	created = models.DateTimeField('Creation Date')
	contact = models.CharField(max_length=200)
	contact_email = models.CharField(max_length=200)
	contact_phone = models.CharField(max_length=200)
	question_text = models.CharField(max_length=200)

class Country(models.Model):

	name = models.CharField(max_length=200)
