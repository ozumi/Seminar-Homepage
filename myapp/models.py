from django.db import models
from django.utils import timezone
# Create your models here.

class Register(models.Model):
	name = models.CharField( max_length=100)
	email = models.CharField( max_length=100)
	phone = models.CharField(max_length=100)
	affiliation = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	create_at = models.DateTimeField(
		default = timezone.now)
	

