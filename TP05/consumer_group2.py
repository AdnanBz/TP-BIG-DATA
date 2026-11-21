import json
from kafka import KafkaConsumer

TOPIC = "campus-sensors"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="tp05-analytics-group", 
    value_deserializer=lambda value: json.loads(value.decode("utf-8")),
    api_version=(2, 5, 0),
)

print(f"Listening with Group 2 to topic: {TOPIC}")

try:
  for message in consumer:
    event = message.value
    print(
        f"[GROUP 2] Partition: {message.partition} |"
        f" Sensor: {event['sensor_id']} | Temp:"
        f" {event['temperature_c']}°C"
    )
except KeyboardInterrupt:
  print("Consumer 2 stopped.")
finally:
  consumer.close()