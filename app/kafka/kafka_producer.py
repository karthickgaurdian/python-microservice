from kafka import KafkaProducer
from app.config import Config , KAFKA_BROKER, KAFKA_TOPIC
from app.logger import logger
import json

def produce_event(data):
    """Send event to Kafka topic"""
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        )
        producer.send(KAFKA_TOPIC, value=data)
        logger.info(f"Sent event: {data}")
        producer.flush()
    except Exception as e:
        logger.error(f"Error sending Kafka event: {e}")

if __name__ == "__main__":
    sample_data = {"message": "Hello from Python Kafka Producer"}
    produce_event(sample_data)
