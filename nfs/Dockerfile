FROM alpine:latest

RUN apk add --no-cache nfs-utils bash

RUN mkdir -p /nfs

RUN chmod 777 /nfs

COPY exports /etc/exports

CMD ["/usr/sbin/rpc.nfsd", "--foreground", "--no-udp", "--no-nfs-version-4"]

EXPOSE 2049 111 20048
