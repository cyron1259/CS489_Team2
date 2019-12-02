from rest_framework import serializers
from .models import Worker, Task, Result

class WorkerSerializer(serializers.ModelSerializer):
    worker_id = serializers.CharField(max_length=30)
    age_group = serializers.CharField(max_length=30)
    gender = serializers.CharField(max_length=30)
    ethnicity = serializers.CharField(max_length=30)
    education = serializers.CharField(max_length=30)
    marital = serializers.CharField(max_length=30)
    income = serializers.CharField(max_length=30)
    employment = serializers.CharField(max_length=30)
    location = serializers.CharField(max_length=30)

    class Meta:
        model = Worker
        fields = ['worker_id', 'age_group', 'gender', 'ethnicity', 'education', 'marital', 'income', 'employment', 'location']

class ResultSerializer(serializers.ModelSerializer):
    worker = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all())
    #worker = serializers.SlugRelatedField(queryset=Worker.objects.all(), slug_field='worker_id')
    task = serializers.SlugRelatedField(queryset=Task.objects.all(), slug_field='task_name')
    value = serializers.IntegerField()

    class Meta:
        model = Result
        fields = ['worker', 'task', 'value']