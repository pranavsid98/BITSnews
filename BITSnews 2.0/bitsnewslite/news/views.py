from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Article, Picture, Video, Event, PollQuestion, PollChoice

# Create your views here.
def index(request):
	article_list = Article.objects.order_by('-article_date')
	picture_list = Picture.objects.all()
	video_list = Video.objects.all()
	pollq_list = PollQuestion.objects.all()
	pollc_list = PollChoice.objects.all()
	#date_list = DateHead.date_now
	template = loader.get_template('news/Home.html')
	context = {
	'article_list': article_list,
	'picture_list': picture_list,
	'video_list': video_list,
	'pollq_list': pollq_list,
	'pollc_list': pollc_list,
	}
	return HttpResponse(template.render(context, request))


def detail(request, article_id):
	article = Article.objects.get(pk=article_id)
	
	#date_list = DateHead.date_now
	return render(request, 'news/post.html', {'article': article})

def posts(request):
	article_list = Article.objects.order_by('-article_date')
	return render(request, 'news/posts.html', {'article_list': article_list})

def event(request):
	events_list = Event.objects.order_by('-event_date')
	return render(request, 'news/events.html', {'events_list': events_list})

def gallery(request):
	picture_list = Picture.objects.all()
	return render(request, 'news/gall.html', {'picture_list': picture_list})

def aboutus(request):
	#date_list = DateHead.date_now
	return render(request, 'news/About.html', {})	

def contri(request):
	#date_list = DateHead.date_now
	return render(request, 'news/Contributors.html', {})		




