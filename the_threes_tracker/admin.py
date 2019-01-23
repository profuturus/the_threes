from django.contrib import admin

# Register your models here.

from the_threes_tracker.models import Topic, Entry


admin.site.register(Topic)
admin.site.register(Entry)

