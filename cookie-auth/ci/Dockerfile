FROM ubuntu:14.04
MAINTAINER promanowski

ARG APP_DIR=/opt/app

RUN apt-get -y -qq update --fix-missing
RUN apt-get -y install \
  zip \
  python python-dev python-pip python-virtualenv \
  git \
  && apt-get clean

COPY . $APP_DIR
WORKDIR $APP_DIR

RUN pip install --upgrade pip && pip install -r ci/requirements.txt
