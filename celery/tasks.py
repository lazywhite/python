from celery import Celery

app = Celery('tasks')
app.config_from_object('celery_config')

@app.task
def add(x,y):
    return x+y



# celery -A tasks worker --loglevel=info
# celery multi start node1 node2 -A tasks  --loglevel=info
