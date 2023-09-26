from celery import Celery
from celery.schedules import crontab
from kombu import Queue

from app.settings import redis_settings


celery_app = Celery(
    __name__,
    backend=redis_settings.url,
    broker=redis_settings.url,
)
celery_app.conf.beat_schedule = {
    'test': {
        'task': 'bot.background_tasks.periodic.test_task.test_task',
        'schedule': crontab(),
    }
}
celery_app.autodiscover_tasks(['bot.background_tasks', 'bot.background_tasks.periodic'], force=True)
