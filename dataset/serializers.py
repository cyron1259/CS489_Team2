from rest_framework import serializers
from .models import Worker, Category, Task, Result

class CategorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=30)
    group = serializers.CharField(max_length=30)

    class Meta:
        model = Category
        fields = ['category', 'group']

class WorkerSerializer(serializers.ModelSerializer):
    worker_id = serializers.CharField(max_length=30)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Worker
        fields = ['worker_id', 'categories']

class ResultSerializer(serializers.ModelSerializer):
    worker = serializers.PrimaryKeyRelatedField(queryset=Worker.objects.all())
    #worker = serializers.SlugRelatedField(queryset=Worker.objects.all(), slug_field='worker_id')
    task = serializers.SlugRelatedField(queryset=Task.objects.all(), slug_field='task_name')
    value = serializers.IntegerField()

    class Meta:
        model = Result
        fields = ['worker', 'task', 'value']