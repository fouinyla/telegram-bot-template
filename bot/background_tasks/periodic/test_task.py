from app.celery import celery_app


@celery_app.task()
def test_task():
    print("WORKS")
