from datetime import datetime, timezone
import json
import random
import time
from kafka import KafkaProducer

TOPIC = "campus-sensors"
BUILDINGS = ["Block-A", "Block-B", "Block-C", "Block-D"]

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda value: json.dumps(value).encode("utf-8"),
    acks="all",
)

try:
  for event_id in range(1, 31):
    event = {
        "event_id": event_id,
        "sensor_id": f"sensor-{random.randint(1, 4):02d}",
        "campus_building": random.choice(BUILDINGS),  
        "temperature_c": round(random.uniform(18, 42), 2),
        "humidity_pct": round(random.uniform(25, 85), 2),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    producer.send(TOPIC, value=event)
    print(f"Sent: {event}")
    time.sleep(1)
  producer.flush()
finally:
  producer.close()