from fastapi import FastAPI, Request
from pydantic import BaseModel
from kafka import KafkaProducer
import json

app = FastAPI()

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

class Message(BaseModel):
    topic: str
    content: dict

@app.post("/publish")
async def publish_message(msg: Message):
    producer.send(msg.topic, msg.content)
    return {"status": "Message sent", "topic": msg.topic}
