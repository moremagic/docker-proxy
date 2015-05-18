FROM ubuntu:14.04

MAINTAINER moremagic<itoumagic@gmail.com>
RUN apt-get update && apt-get upgrade -y && apt-get clean

# ssh install
RUN apt-get update && apt-get install -y openssh-server openssh-client && apt-get clean
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# python3 install
RUN apt-get install -y python3 python3-pip && apt-get clean
RUN pip3 install redis
ADD regist.py /usr/sbin/regist.py
RUN chmod +x  /usr/sbin/regist.py

# Java install
RUN apt-get install -q -y openjdk-7-jre-headless openjdk-7-jdk && apt-get clean
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/
ENV PATH $JAVA_HOME/bin:$PATH

# redis install
RUN apt-get update -y && apt-get dist-upgrade -fy && apt-get clean
RUN apt-get install -fy redis-server
ADD redis.conf /etc/redis/redis.conf

RUN printf '#!/bin/bash \n\
/usr/sbin/regist.py > /var/log/docker-regist.log & \n\
/usr/bin/redis-server & \n\
/usr/sbin/sshd -D \n\
tail -f /var/null \n\
' >> /etc/service.sh \
    && chmod +x /etc/service.sh

EXPOSE 22 80
CMD /etc/service.sh

