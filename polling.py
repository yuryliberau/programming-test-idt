import requests
import time
import signal
import sys

URL = 'https://www.wikipedia.com'
WAIT_SECONDS = 1

# A function that periodically polls a designated web address
def poll():
    r = requests.get(URL, timeout=5)
    print(r.status_code, r.elapsed.total_seconds())
    if r:
        print('Response OK')
    else:
        print('Response Failed')

# Needed just to handle Ctrl+C without raising KeyboardInterrupt exception
def signal_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    poll()
    time.sleep(WAIT_SECONDS)