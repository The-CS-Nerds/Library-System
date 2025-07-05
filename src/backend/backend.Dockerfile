FROM python:3-alpine3.21

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --require-hashes -r requirements.txt

RUN adduser --disabled-password --gecos '' appuser \
 && chown -R appuser /src
USER appuser

ADD ./* ./
