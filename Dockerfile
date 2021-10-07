FROM python:3.8-slim-buster

RUN mkdir /app

ADD requirements.txt /app

WORKDIR /app

RUN apt-get update && apt-get install -y gcc
RUN pip install -r requirements.txt

ADD . /app

ENTRYPOINT [ "python" ]

CMD [ "app/main.py" ]
