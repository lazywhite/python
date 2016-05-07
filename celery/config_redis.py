BROKER_URL = 'redis://localhost:6379/0'

BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': 3600,
    'fanout_prefix': True,
    'fanout_patterns': True,
    }  # 1 hour.
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_ROUTE={
        'tasks.add':'low-priority',
        }
CELERY_ANNOTATIONS = {
        'tasks.add':{'rate_limit':'1000/m'}
        }
