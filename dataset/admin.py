from django.contrib import admin

from .models import Worker, Task, Result

admin.site.register(Worker)
admin.site.register(Task)
admin.site.register(Result)