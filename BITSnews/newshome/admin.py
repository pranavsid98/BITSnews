from django.contrib import admin

# Register your models here.
from .models import Article, Picture, Video,Marquee, PollQuestion, PollChoice, Event
admin.site.register(Article)
admin.site.register(Picture)
admin.site.register(Video)
admin.site.register(Marquee)
admin.site.register(Event)

class ChoiceInLine(admin.TabularInline):
	model = PollChoice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['poll_question']}),
		('Date information', {'fields': ['poll_date'], 'classes': ['collapse']})
	]
	inlines = [ChoiceInLine]


admin.site.register(PollQuestion,QuestionAdmin)
