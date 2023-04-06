# Dockerfile, Image, Container

FROM python:latest

COPY ./requirements.txt /requirements.txt

COPY . .

WORKDIR /

RUN pip install -r requirements.txt

COPY GUI1.py /

CMD ["python", "./GUI1.py"]