from django.contrib import admin

from .models import Worker, Category, Task, Result

admin.site.register(Worker)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Result)