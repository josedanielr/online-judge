#!/bin/bash

# build static files
echo -e '\n\n### Collecting static files\n'
python manage.py collectstatic --no-input

# TODO: requires gettext (this can be done on build)
# echo -e '\n\n### Compiling messages\n'
# python manage.py compilemessages

# TODO: depends on previous step
# echo -e '\n\n### Collecting jsi18n\n'
# python manage.py compilejsi18n

# upgrade db (if any)
echo -e '\n\n### Running DB migrations\n'
# python manage.py migrate

# echo -e '\n\n### Loading fixtures\n'
# python manage.py loaddata navbar
# python manage.py loaddata language_small
# python manage.py loaddata demo

echo -e '\n\n### Initialization completed!\n'

# execute any command passed as parameter
"$@"
