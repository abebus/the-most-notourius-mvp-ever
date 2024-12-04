FROM python:slim

WORKDIR /usr/src/app

COPY predictor .

RUN pip install poetry

ARG DEV_DEPS=False

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction --no-ansi 

WORKDIR /usr/src/app/src

CMD ["main.py"]