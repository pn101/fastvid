migrate:
	- python fastvid/manage.py makemigrations users
	- python fastvid/manage.py migrate
test:
	- python fastvid/manage.py test fastvid users
