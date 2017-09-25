#!/bin/bash

DOCKER_CID=$(docker ps | grep "billmeyer/mongodb" | awk '{print $1}')
MONGO_IP=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' $DOCKER_CID)

docker run --name teste -it -p 0.0.0.0:8080:8080 gregorio/teste --peer ${MONGO_IP} 
