import json
from kafka import KafkaConsumer

TOPIC = "campus-sensors"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="tp05-campus-monitor",
    value_deserializer=lambda value: json.loads(value.decode("utf-8")),
    api_version=(2, 5, 0),
)

print(f"Listening to topic: {TOPIC}")

total_temp = 0.0
count = 0

try:
  for message in consumer:
    event = message.value
    building = event.get("campus_building", "N/A")
    temperature = event["temperature_c"]
    humidity = event["humidity_pct"]

    total_temp += temperature
    count += 1
    running_avg = total_temp / count

    print(
        f"{event['timestamp']} | Building: {building} | "
        f"{event['sensor_id']} | T={temperature}°C | "
        f"RH={humidity}% | Avg={running_avg:.2f}°C"
    )

    if temperature >= 35:
      print("ALERT: High temperature detected!")
except KeyboardInterrupt:
  print("Consumer stopped by user.")
finally:
  consumer.close()