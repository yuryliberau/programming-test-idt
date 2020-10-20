# README #

Initial task:

As a part of a web service monitoring application written in your favorite language, write a function that periodically polls a web address (www.wikipedia.com). The expected response from the web address is HTTP status code 200. Log the status with the time it took to make the query to stdout.

### Dependencies / Requirements

* `Python 2.7 & 3.5+.`
* Install the `requests` library by issuing the following command: `python -m pip install requests`

### Running the application
* The URL we are polling is set to https://www.wikipedia.com, the polling interval is set to 1 second.
* The application can be started by issuing the following command: `python polling.py` <br/>
* To interrupt the process press `CTRL+C`

### Why are we adding dependency on the [requests](https://github.com/psf/requests) library?

We may use `urllib` which is a native python library, but we are using `requests`.
Requests is one of the most downloaded Python package today, it allows us to send HTTP/1.1 requests extremely easily and completely suits our needs.