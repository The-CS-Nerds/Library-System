FROM python:3-alpine3.21

ADD src/* ./src/
ADD setup/* ./setup/
ADD config/* ./config/
ADD requirements.txt ./

RUN pip install -r requirements.txt
CMD ["python", "src/__main__.py"]
