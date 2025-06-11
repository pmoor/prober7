FROM python:alpine
USER nobody

LABEL org.opencontainers.image.authors="patrick@moor.ws"
LABEL org.opencontainers.image.title="Init7 Prober"
LABEL org.opencontainers.image.description="Unofficial container image for the Init7 prober at http://prober7.zekjur.net/"
LABEL org.opencontainers.image.url="https://github.com/pmoor/prober7"

COPY prober.py /prober.py

STOPSIGNAL SIGINT

CMD ["/prober.py"]

