import json
import threading
import signal
import sys
from kafka import KafkaConsumer
from app.config import Config
from app.logger import logger

# Global flag to stop the consumer gracefully
running = True

def consume_events():
    """Starts Kafka consumer in a separate thread and listens to messages."""
    global running
    try:
        consumer = KafkaConsumer(
            Config.KAFKA_TOPIC,
            bootstrap_servers=Config.KAFKA_BROKER,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset="earliest",
            enable_auto_commit=True
        )

        logger.info(f"✅ Listening to Kafka Topic: {Config.KAFKA_TOPIC}")

        for message in consumer:
            if not running:
                break
            logger.info(f"📩 Received: {message.value}")

    except Exception as e:
        logger.error(f"❌ Kafka Error: {e}")

    finally:
        consumer.close()
        logger.info("⚠️ Kafka Consumer Stopped.")

def stop_consumer():
    """Stops the Kafka consumer gracefully."""
    global running
    running = False
    logger.info("🛑 Stopping Kafka Consumer...")

# Handle SIGINT (Ctrl+C) and SIGTERM (Container Stop)
def signal_handler(sig, frame):
    stop_consumer()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
