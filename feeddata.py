import json
from dataset.models import Worker, Task, Result

def addWorker():
    with open('hit.json') as infile:
        data = json.load(infile)
        for entry in data:
            w = Worker(worker_id=entry['workerId'],
                age_group=entry['demographic']['age'],
                gender=entry['demographic']['gender'],
                ethnicity=entry['demographic']['ethnicity'],
                education=entry['demographic']['education'],
                marital=entry['demographic']['marital'],
                income=entry['demographic']['income'],
                employment=entry['demographic']['employment'],
                location=entry['demographic']['location'])
            w.save()

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