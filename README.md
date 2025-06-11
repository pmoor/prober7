# Init7 Prober

An unofficial container image for the Init7 prober at https://prober7.zekjur.net/

Hosted on docker hub: https://hub.docker.com/r/pmoor/prober7

Sources on GitHub: https://github.com/pmoor/prober7

Add `PROBE_ID=0x1234567` to the environment and start the container to have it poll both IPv4 and IPv6 endpoints once a minute.

Example:

```sh
$ podman \
  run \
  -d \
  --rm \
  --env=PROBE_ID=0x12345678 \
  --name=prober7 \
  --log-driver=k8s-file \
  docker://docker.io/pmoor/prober7
```

To build and publish a new image (as a reminder for myself):

```sh
$ podman build -t pmoor/prober7 .
$ podman login -u <user> docker.io
$ podman push localhost/pmoor/prober7:latest docker://docker.io/pmoor/prober7
```

