FROM python:slim

COPY predictor .

CMD ["main.py"]