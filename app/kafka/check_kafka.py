from kafka import KafkaAdminClient, KafkaConsumer
from app.config import Config , KAFKA_BROKER
from app.logger import logger

def check_kafka():
    """Check Kafka broker connection and list topics"""
    try:
        # admin_client = KafkaAdminClient(bootstrap_servers=Config.BROKER)
        consumer = KafkaConsumer(bootstrap_servers=KAFKA_BROKER)
        
        topics = consumer.topics()
        logger.info(f"Connected to Kafka. Available Topics: {topics}")

    except Exception as e:
        logger.error(f"Error connecting to Kafka: {e}")

if __name__ == "__main__":
    check_kafka()
