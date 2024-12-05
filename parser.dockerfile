FROM baseimg

COPY parser .

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction --no-ansi 

WORKDIR ./cian

CMD ["poetry", "run", "scrapyrt", "-s", "ASYNCIO_EVENT_LOOP='uvloop.Loop'", "-s", "LOG_FILE=/logs/parser.log", "-s", "LOG_LEVEL='DEBUG'", "-i", "0.0.0.0"]