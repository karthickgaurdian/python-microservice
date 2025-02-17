from flask import Blueprint, request, jsonify
from app.logger import logger

webhook_blueprint = Blueprint("webhook", __name__)

@webhook_blueprint.route("/webhook", methods=["POST"])
def receive_webhook():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "Invalid JSON"}), 400
        
        logger.info(f"Received webhook data: {data}")
        
        return jsonify({"status": "success", "message": "Data received"}), 200

    except Exception as e:
        logger.error(f"Webhook processing error: {e}")
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500
