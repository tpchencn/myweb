from django.contrib import admin
from learning_logs.models import Topic, Entry, ReadNote, Books

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Books)
admin.site.register(ReadNote)
