FROM nginx:stable-alpine

RUN mkdir -p /dmoj/default

COPY .docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY robots.txt 502.html /dmoj/default/
COPY resources/icons/* /dmoj/default/
