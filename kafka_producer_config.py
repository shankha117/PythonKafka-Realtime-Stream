import confluent_kafka

def get_producer():
    bootstrap_servers = 'localhost:9092'
    conf = {'bootstrap.servers': bootstrap_servers}
    producer = confluent_kafka.Producer(**conf)
    topic = 'testBusdatac'
