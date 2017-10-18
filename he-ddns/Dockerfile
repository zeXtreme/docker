FROM alpine:3.6
LABEL maintainer="zerozwy@gmail.com"

ENV hostname=dyn.example.com
ENV password=password

WORKDIR /

COPY heddns.py ./heddns.py
RUN apk update && apk add python py-pip && pip install requests

ENTRYPOINT ["/usr/bin/python /heddns.py"]
