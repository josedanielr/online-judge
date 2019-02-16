FROM python:2.7

ENV PYHTONUNBUFFERED 1

# remove this if you don't need Nexus UCLV
COPY docker_conf/pip.conf /etc/

RUN mkdir -p /dmoj/webapp
WORKDIR /dmoj

RUN pip install --upgrade pip

# this is for agilizing container creation after changes in project,
# as long as the requirements.txt doesn't change
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ webapp/
WORKDIR /dmoj/webapp

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]