import datetime

from django.db import models #from django db module, import the models class
from django.utils import timezone


class Question(models.Model): #create a class that inherits from the models class
	question_text = models.CharField(max_length = 200) 	
	pub_date = models.DateTimeField('date published')	

	def __unicode__(self):
		return self.question_text


	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

	was_published_recently.admin_order_field = 'pub_date' 
	was_published_recently.boolean = True #replace boolean text value in admin page with check and cross icons
	was_published_recently.short_description = "Published Recently?" #assign a short description as the resultant column's header in the admin page.
	#this makes non-database field generated in the admin interface can be sorted using a specific database field


class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.choice_text