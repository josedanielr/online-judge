#!/bin/sh

echo -e '\n\n### Loading fixtures\n'
python manage.py loaddata navbar
python manage.py loaddata language_small
python manage.py loaddata demo

echo -e '\n\n### Creating super user\n'
python manage.py createsuperuser
