from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# MongoDB setup
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["messaging"]
collection = db["logs"]

# Kafka consumer setup
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='log-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer started. Listening to 'my-topic'...")

for message in consumer:
    print("Received:", message.value)
    collection.insert_one(message.value)
