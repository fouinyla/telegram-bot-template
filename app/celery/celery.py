from celery import Celery
from kombu import Queue

from settings import REDIS, RABBITMQ


celery_app = Celery(
    __name__,
    backend=REDIS,
    broker=RABBITMQ,
)
celery_app.conf.task_queues = (
    Queue("light", routing_key="light"),
    Queue("heavy", routing_key="heavy"),
)
celery_app.autodiscover_tasks(['app.celery.tasks'], force=True)
