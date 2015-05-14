FROM ubuntu:trusty

RUN apt-get update -y && apt-get dist-upgrade -fy
RUN apt-get install -fy python3 python3-pip
RUN pip3 install docker-py redis
ADD linkd /usr/bin/linkd
RUN chmod +x /usr/bin/linkd
