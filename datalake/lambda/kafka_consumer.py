from kafka import KafkaConsumer

def main():
    TOPIC_NAME = "ticket_sales"
    KAFKA_HOST = "kafka:29092"
    
    consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_HOST)
    
    for message in consumer:
        print(message)


if __name__ == "__main__":
    main()
