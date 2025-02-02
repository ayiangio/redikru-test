import time
import random

from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


endpoints = ("one", "two", "three", "four", "five", "error")
# Decorators for metrics
metrics_counter = metrics.counter(
    'http_request_count', 'Total count of HTTP requests', labels={'endpoint': lambda: request.endpoint}
)


@app.route("/one")
@metrics_counter
def first_route():
    time.sleep(random.random() * 0.2)
    return "ok"


@app.route("/two")
def the_second():
    time.sleep(random.random() * 0.4)
    return "ok"


@app.route("/error")
def oops():
    return ":(", 500


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)