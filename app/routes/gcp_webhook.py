from flask import Blueprint, request, jsonify

gcp_webhook = Blueprint("gcp_webhook", __name__)

@gcp_webhook.route("/gcp-webhook", methods=["POST"])
def receive_json():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data received"}), 400
        
        print("Received JSON from GCP:", data)
        
        # Process the data (e.g., forward to Kafka, save to DB, etc.)

        return jsonify({"message": "Received successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
