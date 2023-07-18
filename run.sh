#!/bin/bash

echo "BEGIN -----------------------"

docker build . -t at

echo "DOCKER BUILD COMPLETE --------------------"

docker run -v ./allure_report:/app/allure_report --rm at

echo "DOCKER RUN COMPLETE --------------------"

cp -r allure_report/ report/
rm -r allure_report/

echo "CLEAR DOCKER container and image ----------------------"

docker image rm at -f

docker ps -a
docker images
echo "DONE ------------------------"

echo "ALLURE-REPORT is LOADED -----------------------"
allure serve report/

