import uuid
from django.contrib.postgres.fields import JSONField
from django.db import models

class Worker(models.Model):
    worker_id = models.CharField(max_length=30)

    def __str__(self):
        return self.worker_id

class Category(models.Model):
    worker = models.ForeignKey(Worker, related_name="categories", on_delete=models.CASCADE)
    category = models.CharField(max_length=30)
    group = models.CharField(max_length=30)

class Task(models.Model):
    task_id = models.CharField(max_length=30)
    task_name = models.CharField(max_length=30)
    workers = models.ManyToManyField(Worker, through='Result')

    def __str__(self):
        return self.task_name

class Result(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    value = models.IntegerField()
