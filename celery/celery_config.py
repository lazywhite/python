BROKER_URL = 'amqp://guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
#CELERY_TIMEZONE = 'Europe/Oslo'
#CELERY_ENABLE_UTC = True
CELERY_ROUTE={
        'tasks.add':'low-priority',
        }
CELERY_ANNOTATIONS = {
        'tasks.add':{'rate_limit':'1000/m'}
        }
