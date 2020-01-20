# FROM python:3.8-alpine
FROM python:3.8

ENV PYHTONUNBUFFERED 1

# Use Nexus UCLV (Optional)
COPY .docker/conf/pip.conf /etc/

RUN mkdir /log && mkdir /code
VOLUME /code
WORKDIR /code

# This is for caching to maintain this step cached
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install uwsgi \
    && pip install -r requirements.txt

RUN pip install -r requirements-github.txt

COPY .docker/site/local_settings.py ./dmoj/

RUN python manage.py migrate \
    && python3 manage.py loaddata navbar \
    && python3 manage.py loaddata language_small

# TODO: compile CSSs here
# ./make_style.sh

ENTRYPOINT ./.docker/site/boot.sh

CMD ["uwsgi", "--ini", "./.docker/uwsgi.ini"]

EXPOSE 3031
