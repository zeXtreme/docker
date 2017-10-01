FROM alpine:3.6
MAINTAINER zeXtreme <zerozwy@gmail.com>

ENV hostname=dyn.example.com
ENV password=password
ENV type=4

WORKDIR /

COPY he-dns-update.sh ./he-dns-update.sh
RUN apk update && apk add ca-certificates curl && chmod +x he-dns-update.sh

ENTRYPOINT ["./he-dns-update.sh"]
