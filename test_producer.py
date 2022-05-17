from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10, 1))

msg = "Message".encode('utf-8')
print("msg:",msg)
producer.send('KafkaTest', msg)
print("发送完成")
