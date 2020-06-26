from django.contrib import admin
from QueryApp.models import Blog, Author, Entry, ThemeBlog, Photo
# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(ThemeBlog)

from simple_history.admin import SimpleHistoryAdmin
from QueryApp.models import Poll, Choice

class PollHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "question", "pub_date"]
    history_list_display = ["question"]

admin.site.register(Poll, PollHistoryAdmin)

class ChoiceAdmin(SimpleHistoryAdmin):
	list_display = ["id", "poll", "choice_text"]
	history_list_display = ["choice_text"]

admin.site.register(Choice, ChoiceAdmin)

from QueryApp.models import PointOfInterest
admin.site.register(PointOfInterest)


admin.site.register(Photo)