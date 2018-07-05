FROM alpine:latest
RUN mkdir /buttdial
COPY requirements.txt /buttdial
COPY buttdial.py /buttdial
COPY buttdial.cfg /buttdial
RUN apk update
RUN apk add python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r /upcheck/requirements.txt

WORKDIR /upcheck