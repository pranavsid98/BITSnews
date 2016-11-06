from django.contrib import admin
from .models import Article, Picture, Video, Event, PollQuestion, PollChoice

admin.site.register(Article)
admin.site.register(Picture)
admin.site.register(Video)
admin.site.register(Event)
admin.site.register(PollQuestion)
admin.site.register(PollChoice)
