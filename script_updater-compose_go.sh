#!/usr/bin/env bash

CWD=$(pwd)

# Make sure we are in the current directory with this script
cd $CWD

# Check for docker-compose.yaml file
if [[ -f "docker-compose.yml" || -f "docker-compose.yaml" ]]
then
# Updae docker containers
docker-compose pull

# Restart docker containers
docker-compose down
docker-compose up -d
else
echo "'docker-compose.yaml' not found, exiting."
exit 1
fi