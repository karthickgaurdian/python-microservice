import click
import threading
import time
from app.kafka.kafka_consumer import consume_events, stop_consumer
from app.kafka.kafka_producer import produce_event
from app.kafka.check_kafka import check_kafka
from app.logger import logger

# Global variable for background listener thread
listener_thread = None

@click.group()
def cli():
    """Kafka Command Line Utility"""
    pass

@cli.command()
def check_kafka_command():
    """Check Kafka Connection & Available Topics"""
    check_kafka()

@cli.command()
def send_empty():
    """Send an Empty JSON to Kafka"""
    produce_event({})
    logger.info("✅ Sent empty JSON message to Kafka")

@click.command()
def start_listener():
    """Start the Kafka listener."""
    thread = threading.Thread(target=consume_events, daemon=True)
    thread.start()
    click.echo("🎧 Kafka Listener started.")

@click.command()
def stop_listener():
    """Stop the Kafka listener."""
    stop_consumer()
    click.echo("🛑 Kafka Listener stopped.")

cli.add_command(start_listener)
cli.add_command(stop_listener)

if __name__ == "__main__":
    cli()


# python -m app.cli check-kafka-command
# python -m app.cli send-empty-json
# python -m app.cli start-listener
# python -m app.cli stop-listener
