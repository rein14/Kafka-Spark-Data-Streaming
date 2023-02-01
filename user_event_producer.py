from datetime import datetime
import json
from kafka import KafkaProducer
import random
import time
import uuid

EVENT_TYPE_LIST = ['buy', 'sell', 'click', 'hover', 'idle_5']

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
              api_version=(3,3,2),
              value_serializer=lambda x: json.dumps(x).encode('utf-8'))
TOPIC_NAME = 'events_topic'

def produce_event():
    """
    Function to produce events
    """
    # UUID produces a universally unique identifier
    return {
        'event_id': str(uuid.uuid4()),
        'event_datetime': datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
        'event_type': random.choice(EVENT_TYPE_LIST)
    }

def send_events():
    while(True):
        data = produce_event()
        time.sleep(3) # simulate some processing logic
        producer.send(TOPIC_NAME, value=data)

if __name__ == '__main__':
    send_events()