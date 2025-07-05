FROM python:3-alpine3.21

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD ./* ./
