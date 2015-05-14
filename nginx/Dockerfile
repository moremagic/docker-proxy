FROM ubuntu:trusty

RUN apt-get update -y && apt-get dist-upgrade -fy
RUN apt-get install -fy lua-nginx-redis nginx-extras
ADD nginx.conf /etc/nginx/nginx.conf