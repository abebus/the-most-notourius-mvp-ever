FROM python:slim
RUN apt update && apt install build-essential -y
WORKDIR /usr/src/app

RUN pip install poetry

ARG DEV_DEPS=False