# TP05: Real-Time Data Streaming using Apache Kafka (Smart-Campus)

This project implements a real-time data streaming pipeline for a smart-campus sensor simulation using Apache Kafka, Docker, and Python.

## Project Structure
- `compose.yaml`: Kafka cluster configuration in KRaft mode (single broker).
- `producer.py`: Generates and streams simulated JSON sensor events (temperature & humidity).
- `consumer.py`: Consumes events in real-time, calculates running averages, and triggers high-temperature alerts ($\ge 35^\circ C$).
- `requirements.txt`: Project dependencies (`kafka-python-ng==2.2.2`).
- `screenshots/`: Visual documentation of test outputs and Kafka topics.

###### Prerequisites & Setup
1. **Docker Desktop**: Ensure Docker is running.
2. **Environment Setup**:
   python -m venv .venv
   #### Windows PowerShell:
   .venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ### Running the Pipeline:
   1. **Start Kafka Cluster**:
   docker compose up -d
   2. **Run Consumer (Terminal 1)**: 
   python consumer.py
   3. **Run producer (Terminal 2)**:
   python producer.py 
   ## Topic Inspection:
   docker exec -it tp05-kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic campus-sensors