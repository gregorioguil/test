#!/bin/bash

docker run --name mongodb -it -e HAB_MONGODB="$(cat mongo.toml)" -p 27017:27017 billmeyer/mongodb
