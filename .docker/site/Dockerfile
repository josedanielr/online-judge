FROM python:3.8-alpine

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

# RUN ./make_style.sh

COPY .docker/site/local_settings.py ./dmoj/

RUN python manage.py migrate

ENTRYPOINT ./.docker/site/boot.sh

CMD ["uwsgi", "--ini", "./.docker/uwsgi.ini"]

EXPOSE 8000
