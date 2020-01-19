#!/bin/bash

python3 manage.py compilemessages

python3 manage.py migrate
python3 manage.py loaddata navbar
python3 manage.py loaddata language_small

python3 manage.py collectstatic --no-input
python3 manage.py compilejsi18n

# execute any command passed as parameter
"$@"
