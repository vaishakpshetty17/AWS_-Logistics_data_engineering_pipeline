from flask import Flask, jsonify
import random
from datetime import datetime
from faker import Faker

app  = Flask(__name__)
fake = Faker()

# Sample locations
locations = ["Bangalore", "Mumbai", "Delhi", "Chennai"]

# Shipment statuses
statuses = ["CREATED", "IN_TRANSIT", "DELAYED", "DELIVERED"]


def generate_shipment():
    return {
        "shipment_id": f"S{random.randint(1000, 9999)}",
        "status": random.choice(statuses),
        "location": random.choice(locations),
        "timestamp": datetime.now().isoformat()
    }

@app.route("/shipment", methods=["GET"])
def get_shipment():
    data = generate_shipment()
    return jsonify(data)

@app.route("/shipments", methods=["GET"])
def get_multiple_shipments():
    data = [generate_shipment() for _ in range(5)]
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)