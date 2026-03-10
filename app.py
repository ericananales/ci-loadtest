from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API is running"})


@app.route("/api/data")
def data():
    # simulate processing time
    delay = random.uniform(0.1, 0.4)
    time.sleep(delay)

    return jsonify({
        "status": "success",
        "delay": delay
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)