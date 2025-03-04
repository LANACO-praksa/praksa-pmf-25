import json

from configs.config import KAFKA_BROKER
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError


def create_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        acks="all",
    )


def send_data_to_topic(producer, topic, value):
    producer.send(topic, value=value)
    print(f"[Kafka] Sent to {topic}: {value}")


def create_kafka_topics():
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKER)

        topic_list = [
            NewTopic(name="client_events", num_partitions=1, replication_factor=1),
            NewTopic(
                name="product_change_events", num_partitions=1, replication_factor=1
            ),
            NewTopic(name="transaction_events", num_partitions=1, replication_factor=1),
        ]

        admin_client.create_topics(topic_list)
        admin_client.close()
        print("Kafka topics created successfully")
    except TopicAlreadyExistsError:
        print("Topic already exists")
    except Exception as e:
        print(f"Error creating Kafka topics: {e}")
