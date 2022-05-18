FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y libpq-dev python-dev

RUN adduser --disabled-password --disabled-login vicsite
USER vicsite

WORKDIR /home/vicsite/app


ENV PATH="/home/vicsite/.local/bin:${PATH}"

COPY --chown=vicsite:vicsite requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --user -r requirements.txt

COPY --chown=vicsite:vicsite . /home/vicsite/app/
