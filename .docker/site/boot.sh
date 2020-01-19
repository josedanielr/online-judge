#!/bin/bash

# build static files
# ./make_style.sh
python3 manage.py collectstatic --no-input
python3 manage.py compilemessages
python3 manage.py compilejsi18n

# upgrade db (if any)
python3 manage.py migrate

# execute any command passed as parameter
"$@"
