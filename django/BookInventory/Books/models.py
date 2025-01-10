from django.db import models
from django.conf import settings

# Create your models here.
class Book(models.Model):
	entry_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	pub_date = models.DateField()
	isbn = models.CharField(max_length=17)

	def __str__(self):
		return self.title

class ProfilePicture(models.Model):
	animal = models.CharField(max_length=50)
	background = models.CharField(max_length=200)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
