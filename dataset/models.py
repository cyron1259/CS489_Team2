import uuid
from django.db import models

class Worker(models.Model):
    worker_id = models.CharField(max_length=30)
    age_group = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    ethnicity = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    marital = models.CharField(max_length=30)
    income = models.CharField(max_length=30)
    employment = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.worker_id

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
