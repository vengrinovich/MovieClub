from django.db import models
from django.utils import timezone

class MovieClub(models.Model):
	privacy_choices = (
		('private', 'Private'),
		('public', 'Public'))
    
	name = models.CharField(max_length=200)
	privacy = models.CharField(max_length=7, choices = privacy_choices)
	created_date = models.DateTimeField(default=timezone.now)

	#logo = models.ImageField(upload_to = 'group_pictures/') add later - reference official django imagefield documentation
	def __str__(self):
		return self.name
