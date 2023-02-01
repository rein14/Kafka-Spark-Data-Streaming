import json
from kafka import KafkaConsumer

TOPIC_NAME = 'events_topic'

consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        group_id="event-collector-group-1p",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )

def consume_events():
    for m in consumer:
        # any custom logic you need
        print(m.value)

if __name__ == '__main__':
    consume_events()