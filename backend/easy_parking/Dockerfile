FROM python:3.9
ENV PYTHONUNBUFFEREDRED 1

WORKDIR /usr/src/app
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/