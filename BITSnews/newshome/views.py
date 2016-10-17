from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Article, Picture, Video, Marquee,Event, PollQuestion, PollChoice, DateHead

# Create your views here.
def index(request):
	article_list = Article.objects.order_by('-article_date')
	picture_list = Picture.objects.all()
	video_list = Video.objects.all()
	marquee_list = Marquee.objects.all()
	events_list = events_list = Event.objects.all()
	pollq_list = PollQuestion.objects.all()
	pollc_list = PollChoice.objects.all()
	date_list = DateHead.date_now
	template = loader.get_template('newshome/index.html')
	context = {
	'article_list': article_list,
	'picture_list': picture_list,
	'video_list': video_list,
	'marquee_list': marquee_list,
	'events_list': events_list,
	'pollq_list': pollq_list,
	'pollc_list': pollc_list,
	'date_list': date_list,
	}
	return HttpResponse(template.render(context, request))

def aboutus(request):
	marquee_list = Marquee.objects.all()
	date_list = DateHead.date_now
	return render(request, 'newshome/aboutus.html', {'marquee_list': marquee_list, 'date_list': date_list})


def detail(request, article_id):
	article = Article.objects.get(pk=article_id)
	marquee_list = Marquee.objects.all()
	date_list = DateHead.date_now
	return render(request, 'newshome/detail.html', {'article': article,'marquee_list': marquee_list, 'date_list': date_list})

def vote(request):
	question = PollQuestion.objects.all()
	try:
		selected_choice = PollChoice.objects.get(pk=request.POST['choice'])
	except(KeyError, PollChoice.DoesNotExist):
		return render(request, 'newshome/index.html', {'question': question, 'error_message': "you didnt select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('newshome:result'))
	


def result(request):
	article_list = Article.objects.order_by('-article_date')
	date_list = DateHead.date_now
	picture_list = Picture.objects.all()
	video_list = Video.objects.all()
	marquee_list = Marquee.objects.all()
	events_list = Event.objects.all()
	question = PollQuestion.objects.all()
	pollc_list = PollChoice.objects.all()
	return render(request, 'newshome/result.html', {'article_list': article_list, 'picture_list': picture_list, 'video_list': video_list, 'marquee_list': marquee_list, 'events_list': events_list, 'question': question, 'pollc_list': pollc_list, 'date_list': date_list})


