# 📡 Real-Time Distributed Messaging System

An event-driven backend using **FastAPI**, **Kafka**, and **MongoDB** to route, consume, and persist messages. Ideal for streaming data pipelines or real-time event logging.

---

## 🧠 Architecture

```plaintext
[REST API] → [Kafka Topic] → [Kafka Consumer] → [MongoDB Logger]
```

---

## 🛠️ Tech Stack
- Python 3.10 + FastAPI
- Kafka + Zookeeper
- MongoDB
- Docker Compose
- GitHub Actions CI/CD

---

## ▶️ Run Locally

```bash
# Start Kafka and MongoDB
cd kafka
docker-compose up -d

# Start FastAPI publisher
cd ../api-service
uvicorn app.main:app --reload

# Start Kafka Consumer
python services/consumer.py
```

---

## 🔁 CI/CD Pipeline
- GitHub Actions installs dependencies
- Builds Docker image
- Pushes to DockerHub using secrets

---

## 📬 Sample API

```http
POST /publish
Content-Type: application/json

{
  "topic": "my-topic",
  "content": {
    "event": "user_signup",
    "user": "jeevan"
  }
}
```

---

## 🏷️ Badges

![Python](https://img.shields.io/badge/python-3.10-blue)
![Kafka](https://img.shields.io/badge/Kafka-event--driven-yellow)
