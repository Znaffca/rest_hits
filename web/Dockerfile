# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# added netcat as a required system dependecy
RUN apt-get update && apt-get install -y apt-utils netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/web/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/web/

ENTRYPOINT [ "/usr/src/web/docker-entrypoint.sh" ]