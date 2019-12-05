import json
from dataset.models import Worker, Category, Task, Result

def addWorker():
    with open('hit.json') as infile, open('metadata.json') as mdfile:
        data = json.load(infile)
        md = json.load(mdfile)
        for entry in data:
            w = Worker(worker_id=entry['workerId'])
            w.save()
            for cat in md["categories"].keys():
                c = Category(worker=w,
                    category=cat,
                    group=entry['demographic'][cat])
                c.save()

def addTask():
    with open('tasks.json') as infile:
        data = json.load(infile)
        for entry in data:
            if entry['value']:
                t = Task(task_id=entry['_id'],task_name=entry['imagename'])
                t.save()
                print(entry['_id'],entry['value'])
                r = Result(worker=Worker.objects.get(worker_id=entry['workerId']),
                    task=t,
                    value=next((i for i, x in enumerate(entry['value']) if x), None)+1)
                r.save()