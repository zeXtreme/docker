FROM python:alpine3.6
LABEL maintainer="zerozwy@gmail.com"

ENV hostname=dyn.example.com
ENV password=password

COPY heddns.py /heddns.py
RUN pip install requests

ENTRYPOINT ["zsh"]
