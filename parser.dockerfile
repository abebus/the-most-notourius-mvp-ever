FROM python:slim

WORKDIR /usr/src/app

COPY parser .

RUN pip install poetry

ARG DEV_DEPS=False

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction --no-ansi 

WORKDIR /usr/src/app/src

CMD ["scrapyrt", "-s", "ASYNCIO_EVENT_LOOP='uvloop.Loop'"]