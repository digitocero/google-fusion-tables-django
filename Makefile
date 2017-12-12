makemigrations:
	./.ve/bin/python3 ./src/manage.py makemigrations
migrate:
	./.ve/bin/python3 ./src/manage.py migrate
run:
	./.ve/bin/python3 ./src/manage.py runserver
createsuperuser:
	./.ve/bin/python3 ./src/manage.py createsuperuser

install:
	python3 -m env ​.ve​
	​./.ve/bin/pip​ install​ -r​ requirements.txt​
	#syncdb is not available anymore in django 1.9
	./.ve/bin/python3 ./src/manage.py migrate
