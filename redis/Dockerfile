FROM ubuntu:trusty

RUN apt-get update -y && apt-get dist-upgrade -fy
RUN apt-get install -fy redis-server
ADD redis.conf /etc/redis/redis.conf