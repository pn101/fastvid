migrate:
	- python fastvid/manage.py makemigrations fastvid users
	- python fastvid/manage.py migrate
test:
	- python fastvid/manage.py test fastvid users
