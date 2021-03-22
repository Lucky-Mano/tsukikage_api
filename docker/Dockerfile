FROM python:3.8-slim

LABEL maintainer "Lucky-Mano <phatbowie@gmail.com>"

ENV DIR=/app

RUN apt-get update && \
  apt-get install --no-install-recommends build-essential -y && \
  pip install -U --no-cache-dir pip setuptools wheel poetry && \
  apt-get autoremove -y && \
  useradd -m shirenger && \
  rm -rf /var/lib/apt/lists/*

USER shirenger

WORKDIR ${DIR}

CMD [ "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "endpoint:api" ]
