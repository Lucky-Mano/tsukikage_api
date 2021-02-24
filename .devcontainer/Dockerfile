FROM python:slim

RUN set -x && \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get install build-essential git -y && \
  pip install -U --no-cache-dir pip setuptools poetry
