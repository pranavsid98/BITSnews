from django.contrib import admin
from .models import Article, Picture, Video, Event, PollQuestion, PollChoice, Category


class ChoiceInline(admin.StackedInline):
	model = Category
	extra = 1

class ArticleAdmin(admin.ModelAdmin):
	inlines = [ChoiceInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Picture)
admin.site.register(Video)
admin.site.register(Event)
admin.site.register(PollQuestion)
admin.site.register(PollChoice)

