import json
import os
from confluent_kafka import Consumer, KafkaError
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/airlinetwin")
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

engine = create_engine(DATABASE_URL)
conf = {
    'bootstrap.servers': KAFKA_BOOTSTR_SERVERS if 'KAFKA_BOOTSTRAP_SERVERS' in os.environ else 'localhost:9092',
    'group.id': 'twinaero-stream-consumer',
    'auto.offset.reset': 'earliest'
}

print("Starting TwinAero Stream Worker...")
