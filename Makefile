migrate:
	- python fastvid/manage.py makemigrations users posts tags notifications
	- python fastvid/manage.py migrate
test:
	- python fastvid/manage.py test fastvid users posts tags notifications
