"""
Flask Web Application
Entry point for the app. Run locally with: python app.py
"""

import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/", methods=["GET"])
def home():
    """Homepage route."""
    return render_template("index.html", title="Python Flask App")


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint - useful for CI/CD, load balancers, uptime monitors."""
    return jsonify({"status": "ok", "service": "python-flask-app"}), 200


@app.route("/api/echo", methods=["POST"])
def echo():
    """Simple example API endpoint that echoes back JSON input."""
    data = request.get_json(silent=True) or {}
    return jsonify({"you_sent": data}), 200


@app.route("/api/greet/<name>", methods=["GET"])
def greet(name):
    """Example dynamic route."""
    return jsonify({"message": f"Hello, {name}!"}), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
