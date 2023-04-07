# Dockerfile, Image, Container

FROM python:latest

COPY ./requirements.txt /requirements.txt

COPY . .

WORKDIR /

RUN pip install -r requirements.txt

COPY GUI2.py /

CMD ["python", "./GUI2.py"]