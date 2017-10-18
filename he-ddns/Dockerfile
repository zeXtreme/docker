FROM python:alpine3.6
LABEL maintainer="zerozwy@gmail.com"

ENV hostname=dyn.example.com
ENV password=password

COPY heddns.py ./heddns.py
RUN apk update && apk add python py-pip && pip install requests && chmod +x heddns.py

ENTRYPOINT [./heddns.py]
