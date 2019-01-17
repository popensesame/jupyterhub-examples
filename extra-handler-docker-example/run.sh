#!/bin/bash

source '.env'

docker run -v $PWD:/srv/jupyterhub --expose 8888 -p 8000:8000 --name $CONTAINER_NAME $IMAGE_NAME


