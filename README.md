Project make on Python 3.10

run bash script
`chmod 777 run.sh`
`sudo sh run.sh` or `sh run.sh` (if you want to open allure report at the end)


## Commands

with junit test report
`python -m pytest --junitxml=junitreport/result.xml`

remove image
`docker image rm <id>`
`docker image rm <image_name> -f`

build image from Dockerfile
`docker build . -t <image_name>`

run autotests in docker container
`docker run --rm <image_name>`
`docker run -v $(pwd)/allure-report:/app/allure-report --rm at`
`docker run -v ./allure_report:/app/allure_report --rm at`

remove all containers
`docker system prune`