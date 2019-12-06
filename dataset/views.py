from django.shortcuts import render
from django.http import JsonResponse
from .models import Worker, Task, Result
from .serializers import WorkerSerializer, ResultSerializer
import json
import os.path

with open(os.path.dirname(__file__) + '/../metadata.json') as mdfile:
    md = json.load(mdfile)
    scale = md['scale']
    categories = md['categories'].keys()

def normalize(v):
    sum = 0
    for x in v:
        sum += x
    
    return [x/sum for x in v]

def compute_Wasserstein(v1, v2):
    d = [0 for i in range(scale + 1)]
    sum = 0
    for i in range(len(v1)):
        d[i + 1] = v1[i] + d[i] - v2[i]
        sum += abs(d[i + 1])
    return sum


distance = {}
group_size = {}
overall_distribution = {}
image_list = []

worker_serializer = WorkerSerializer(Worker.objects.all(), many=True)
result_serializer = ResultSerializer(Result.objects.all(), many=True)

for category in categories:
    distance[category] = {}
    group_size[category] = {}

worker_list = worker_serializer.data
result_list = result_serializer.data

for worker in worker_list:
    for category_dict in worker['categories']:
        category = category_dict['category']
        if category_dict['group'] not in group_size[category]:
            group_size[category][category_dict['group']] = 0
        group_size[category][category_dict['group']] += 1

for result in result_list:
    if result['task'].startswith('img') and result['task'] not in image_list:
        image_list.append(result['task'])
    for category in categories:

        for category_dict in worker_list[result['worker'] - 1]['categories']:
            if category == category_dict['category']:
                group = category_dict['group']
                break

        if group not in distance[category]:
            distance[category][group] = {}
        
        if result['task'] not in distance[category][group]:
            distance[category][group][result['task']] = {'count': 0, 'distribution': [0 for i in range(scale)]}

        if result['task'] not in overall_distribution:
            overall_distribution[result['task']] = {'distribution': [0 for i in range(scale)]}

        if 'workers' not in distance[category][group][result['task']]:
            distance[category][group][result['task']]['workers'] = {}
            for i in range(5):
                distance[category][group][result['task']]['workers'][str(i+1)] = []
        
        distance[category][group][result['task']]['count'] += 1
        distance[category][group][result['task']]['distribution'][result['value'] - 1] += 1
        distance[category][group][result['task']]['workers'][str(result['value'])].append(result['worker'])
    overall_distribution[result['task']]['distribution'][result['value'] - 1] += 1

for category in categories:
    for group in distance[category].keys():
        for image in distance[category][group].keys():
            v1 = distance[category][group][image]['distribution']
            v2 = overall_distribution[image]['distribution']
            distance[category][group][image]['distance'] = compute_Wasserstein(normalize(v1), normalize(v2))


for category in categories:
    for group in distance[category].keys():
        min = scale - 1
        max = 0
        sum = 0
        count = 0
        for image in distance[category][group].keys():
            dist = distance[category][group][image]['distance']
            if min > dist:
                min = dist
            if max < dist:
                max = dist
            sum += dist
            count += 1
        distance[category][group]['min'] = min
        distance[category][group]['max'] = max
        distance[category][group]['avg'] = sum / count

def category_list(request):
    return JsonResponse({'categories': list(categories)})

def category_stats(request, category):
    stats = {}
    for group in distance[category].keys():
        stats[group] = {}
        stats[group]['count'] = group_size[category][group]
        stats[group]['min'] = distance[category][group]['min']
        stats[group]['max'] = distance[category][group]['max']
        stats[group]['avg'] = distance[category][group]['avg']
    return JsonResponse(stats)

def group_dist(request, group):
    stats = {}
    for category in categories:
        if group in distance[category]:
            for image in image_list:
                if image in distance[category][group]:
                    stats[image] = distance[category][group][image]['distance']
    return JsonResponse(stats)

def image_dist(request, image, group):
    for category in categories:
        if group in distance[category]:
            if image in distance[category][group]:
                ret = {
                    'id': image,
                    'group': group,
                    'uri': request.get_host() + '/static/images/'+image+'.jpg',
                    'overallDistribution': overall_distribution[image]['distribution'],
                    'selectedDistribution': distance[category][group][image]['distribution'],
                    'workers': distance[category][group][image]['workers']
                }
            else:
                ret = {}
            return JsonResponse(ret)
    