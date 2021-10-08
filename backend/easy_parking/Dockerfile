FROM python:3
ENV PYTHONUNBUFFEREDRED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/