from django.db import models
from django.utils import timezone

		
class User(models.Model):
	name = models.CharField(max_length=50)
	mail = models.CharField(max_length=50)
	nickname = models.CharField(max_length=50)
	def __str__ (self):
		return self.name
		
	@property
	def fullname(self):
		return self.name + " [" + self.nickname + "]"
	
class Post(models.Model):
	
	title = models.CharField(max_length=200)
	lead = models.CharField(max_length=10, default='default')
	tag = models.CharField(max_length=20, default=' ')
	text = models.TextField()
	created_date = models.DateField()
	published_date = models.DateField()
	user = models.ForeignKey(User, related_name="User", null=True)
	

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title