web: gunicorn --pythonpath fastvid/ --bind :4050 --workers=3 fastvid.wsgi
worker: celery --workdir=fastvid/ --app=fastvid.celery:app --concurrency=3 worker
flower: celery --workdir=fastvid/ --app=fastvid.celery:app flower
