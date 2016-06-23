migrate:
	- python fastvid/manage.py makemigrations users posts
	- python fastvid/manage.py migrate
test:
	- python fastvid/manage.py test fastvid users posts
