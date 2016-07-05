web: gunicorn --pythonpath fastvid/ --bind :4050 --workers=3 fastvid.wgsi
worker: celery --workdir=fastvid/ --app=fastvid.celery:app --concurrency=3 worker
flower: celery --workdir=fastvid/ --app=fastvid.celery:app flower
