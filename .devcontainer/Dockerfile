FROM python:slim

RUN set -x && \
  apt-get update && \
  apt-get install --no-install-recommends build-essential git -y && \
  pip install -U --no-cache-dir pip setuptools uv && \
  apt-get autoremove -y && \
  rm -rf /var/lib/apt/lists/*
