from django.db import models
import datetime

# Create your models here.

class Ticker(models.Model):
	ticker_text = models.CharField(max_length=100)
	def __str__(self):
		return self.ticker_text

class Article(models.Model):
	article_title = models.CharField(max_length=100)
	article_text = models.TextField()
	article_author = models.CharField(max_length=40)
	article_image = models.CharField(max_length=100)
	article_date = models.DateTimeField('date published')
	article_summary = models.TextField(default="I wil put in shit, wait! ")
	def __str__(self):
		return self.article_title

class Category(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	TECHNOLOGY = 'TECH'		
	OASIS = 'OASIS'
	DEPARTMENTS = 'DEP'
	CLUBS = 'CLUB'
	ACADEMICS = 'ACADS'
	CATEGORY_CHOICES = (
			(TECHNOLOGY, 'Technology'),
			(OASIS, 'Oasis'),
			(DEPARTMENTS, 'Departments'),
			(CLUBS, 'Clubs'),
			(ACADEMICS, 'Academics'),
		)
	category = models.CharField(
			max_length = 10,
			choices = CATEGORY_CHOICES,
		)
	def __str__(self):
		return self.category

class Picture(models.Model):
	pics_image = models.CharField(max_length=100)
	def __str__(self):
		return self.pics_image

class Video(models.Model):
	video_video = models.CharField(max_length=200)
	def __str__(self):
		return self.video_video


class Event(models.Model):
	event_title = models.CharField(max_length=100)
	event_summary = models.TextField(default=" I will put in shit, wait")
	event_location = models.CharField(max_length=30)
	event_date = models.DateTimeField('date of event')
	event_image = models.CharField(max_length=100, null=True, blank=True)
	def __str__(self):
		return self.event_image

class PollQuestion(models.Model):
	poll_question = models.CharField(max_length=200)
	poll_date = models.DateTimeField('date published')

class PollChoice(models.Model):
	question = models.ForeignKey(PollQuestion, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

#class DateHead(models.Model):
#	date_now = datetime.datetime.now()






