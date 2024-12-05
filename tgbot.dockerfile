FROM baseimg

COPY tgbot .

RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction --no-ansi 

CMD ["poetry", "run", "python", "main.py"]