from celery import Celery

from settings import REDIS, RABBITMQ


celery_app = Celery(
    __name__,
    backend=REDIS,
    broker=RABBITMQ
)

celery_app.autodiscover_tasks(['app.celery.tasks'], force=True)
