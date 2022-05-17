from kafka import KafkaConsumer

consumer = KafkaConsumer('KafkaTest', bootstrap_servers=['localhost:9092'], api_version=(0, 10, 1))

for msg in consumer:
    recv = f"Topic: {msg.topic}, Partition: {msg.partition}, Key: {msg.key}, Value: {msg.value}"
    print(recv)