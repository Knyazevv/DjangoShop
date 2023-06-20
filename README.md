# DjangoShop

python -m venv env

.\env\Scripts\activate

pip install -r requirements.txt

cd .\shop\

python manage.py runserver

При додаванні нових пакетів в venv

pip freeze > requirements.txt

pip install django_compressor

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
