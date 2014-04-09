from django.db import models

# Create your models here.



class Client(models.Model):
	name=models.CharField(max_length=100)
	contact_person=models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

USE_IN = (
	(0 , 'Don\'t show'),
	(1 , 'Show small'),
	(2 , 'Show in Highlights'),
)

class Project(models.Model):
	name=models.CharField(max_length=100)
	text=models.TextField()
	link=models.CharField(max_length=255)
	link_display=models.CharField(max_length=100)
	default_large=models.ForeignKey('Image', related_name='default_large',blank=True,null=True)
	default_medium=models.ForeignKey('Image', related_name='default_medium',blank=True, null=True)
	default_small=models.ForeignKey('Image',related_name='default_small', blank=True, null=True)
	client=models.ForeignKey('Client')
	use_in = models.IntegerField(choices=USE_IN, default=2)
	what_we_did=models.TextField()
	def __unicode__(self):
		return self.name


class Image(models.Model):
	file=models.ImageField(upload_to='portfolio_images')
	project=models.ForeignKey('Project')
	size=models.CharField(max_length=100) # options large500, medium300, small100
	def __unicode__(self):
		return self.project.client.name + ": " + self.size
	
	
