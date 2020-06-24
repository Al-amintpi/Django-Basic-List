from django.contrib import admin
from QueryApp.models import Blog, Author, Entry, ThemeBlog
# Register your models here.
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
admin.site.register(ThemeBlog)


