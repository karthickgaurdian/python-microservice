from app.config import Config

# Kafka settings
KAFKA_BROKER = Config.BROKER
TOPIC_NAME = Config.TOPIC

# Import Kafka modules so they can be used easily
from .kafka_consumer import KafkaConsumer
from .kafka_producer import KafkaProducer
