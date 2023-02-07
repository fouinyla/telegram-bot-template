from celery import Celery

from settings import REDIS, RABBITMQ


celery_app = Celery(__name__)
celery_app.conf.broker_url = RABBITMQ
celery_app.conf.result_backend = REDIS
celery_app.autodiscover_tasks(['app.celery.tasks'], force=True)
