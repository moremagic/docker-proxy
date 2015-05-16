# docker-proxy

つくりちゅうです。。。


起動メモ
docker run -d -p :6379 --name redis {redis-container} /usr/bin/redis-server
docker run -d -e DOCKER_HOST=192.168.1.6:4243 --link redis:redis -P {nginx-container}
