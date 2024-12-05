FROM baseimg

COPY predictor .
COPY .static .static
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction --no-ansi 

CMD ["poetry", "run", "uvicorn", "main:app","--host", "0.0.0.0"]