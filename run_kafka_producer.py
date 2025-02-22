from app.kafka.kafka_producer import produce_event

if __name__ == "__main__":
    sample_data = {"event": "test_event", "status": "success"}
    produce_event(sample_data)
