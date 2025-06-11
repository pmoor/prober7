#!/usr/local/bin/python3

from time import time, sleep
from random import random
import logging
import sys
import urllib.request
import urllib.error
import os

logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger("prober")

PROBE_ID = os.environ.get("PROBE_ID")
if not PROBE_ID:
  print("PROBE_ID environment variable not found")
  sys.exit(1)

logger.info("Using Probe ID \"%s\"" % PROBE_ID)

URLS = [
  "http://prober7-sink.zekjur.net:42070/lightprobe/" + PROBE_ID,
  "http://prober7-sink6.zekjur.net:42070/lightprobe/" + PROBE_ID,
]

start = time()
i = 0
while True:
  logger.info("iteration %d start" % i)
  start += (random() - 0.5) + 60

  for url in URLS:
    try:
      urllib.request.urlopen(url, timeout=20)
    except urllib.error.URLError as e:
      logger.warning("failed to fetch %s: %s" % (url, e))

  diff = max(10, start - time())
  sleep(diff)
  i += 1 
