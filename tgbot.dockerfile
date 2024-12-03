FROM python:slim

COPY tgbot .

CMD ["main.py"]