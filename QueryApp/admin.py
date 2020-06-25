from django.contrib import admin
from QueryApp.models import Blog, Author, Entry, ThemeBlog
# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(ThemeBlog)

from simple_history.admin import SimpleHistoryAdmin
from QueryApp.models import Poll, Choice

class PollHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "question", "pub_date"]
    history_list_display = ["status"]

admin.site.register(Poll, PollHistoryAdmin)
admin.site.register(Choice, SimpleHistoryAdmin)

