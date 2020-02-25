FROM josedrm/nodesource as builder

RUN mkdir /usr/etc
COPY .docker/conf/npmrc /usr/etc
RUN npm install -g sass postcss-cli autoprefixer

# Compile SASS sources
COPY resources resources/
COPY make_style.sh .
RUN ./make_style.sh


FROM python:3.8

EXPOSE 3031
VOLUME /dmoj/log /dmoj/static

ENV PYHTONUNBUFFERED 1

# Use a local Nexus as mirror
COPY .docker/conf/pip.conf /etc

COPY requirements.txt requirements-github.txt ./

RUN pip install --upgrade pip \
    && pip install -r requirements-github.txt \
    && rm requirements-github.txt

RUN pip install uwsgi python-memcached \
    && pip install -r requirements.txt \
    && rm requirements.txt

RUN mkdir -p /dmoj/log /dmoj/code
WORKDIR /dmoj/code

COPY . .
COPY --from=builder resources resources/

COPY .docker/site/uwsgi.ini ../
COPY .docker/site/boot.sh ../

ENTRYPOINT ["../boot.sh"]

CMD ["uwsgi", "--ini", "../uwsgi.ini"]
