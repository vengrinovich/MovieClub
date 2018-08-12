from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class MovieClub(models.Model):
	privacy_choices = (
		('private', 'Private'),
		('public', 'Public'))
    
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	privacy = models.CharField(max_length=7, choices = privacy_choices)
	created_date = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(MovieClub, self).save(*args, **kwargs)

	#logo = models.ImageField(upload_to = 'group_pictures/') add later - reference official django imagefield documentation
	def __str__(self):
		return self.name
