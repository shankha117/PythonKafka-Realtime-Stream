
import json
from datetime import datetime
import uuid

# read the coordinates from file
with open('./data/bus1.json') as f:
    data = json.load(f)

coordinates = data['features'][0]['geometry']['coordinates']

# kafka Producer
import confluent_kafka
bootstrap_servers = 'localhost:9092'
conf = {'bootstrap.servers': bootstrap_servers}
producer = confluent_kafka.Producer(**conf)
topic = 'testBusdatac'

# message structure for bus1
message_data = {}
message_data['busline'] = '00001'

import time
def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):
        try:
            message_data['key'] = message_data['busline'] + "_" + str(uuid.uuid4().hex)
            message_data['timestamp'] = str(datetime.utcnow())
            message_data['lat'] = coordinates[i][1]
            message_data['long'] = coordinates[i][0]
            message = json.dumps(message_data).encode()


            producer.produce(topic, message)

            time.sleep(0.5)

            print(message)

            if i == len(coordinates) - 1:
                i = 0
            else:
                i += 1
        except BufferError as e:
            print('Buffer error, the queue must be full! Flushing...')
            producer.flush()

            print('Queue flushed, will write the message again')
            producer.produce(
                topic=topic,
                value=message,
            )

generate_checkpoint(coordinates)

"""
client = KafkaClient(hosts="localhost:9092")
print(client.topics['test_topic'.encode()])
topic = client.topics['testBusdatac'.encode()]
producer = topic.get_sync_producer()
i = 0
while True:
    message = ('message' + str(i)).encode('ascii')
    producer.produce(message)
    i += 1
"""


# client = KafkaClient(hosts="localhost:9092")
# topic = client.topics[b'testBusdatac']
# with topic.get_sync_producer() as producer:
#     for i in range(4):
#         producer.produce(b'test message{0}')


# bootstrap_servers = 'localhost:9092'
# msg_count = 1000000
# msg_size = 100
# msg_payload = ('kafkatest' * 20).encode()[:msg_size]
# print(msg_payload)
# print(len(msg_payload))
#
# from kafka import KafkaProducer
#
# import time
# producer_timings = {}
# consumer_timings = {}
#
# def calculate_thoughput(timing, n_messages=1000000, msg_size=100):
#     print("Processed {0} messsages in {1:.2f} seconds".format(n_messages, timing))
#     print("{0:.2f} MB/s".format((msg_size * n_messages) / timing / (1024*1024)))
#     print("{0:.2f} Msgs/s".format(n_messages / timing))
#
# # def python_kafka_producer_performance():
# #     producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
# #
# #     producer_start = time.time()
# #     topic = 'testBusdatac'
# #     for i in range(msg_count):
# #         producer.send(topic, msg_payload)
# #
# #     producer.flush()  # clear all local buffers and produce pending messages
# #
# #     return time.time() - producer_start
# #
# # producer_timings['python_kafka_producer'] = python_kafka_producer_performance()
# # calculate_thoughput(producer_timings['python_kafka_producer'])
#
#
#
# import confluent_kafka
# topic = 'testBusdatac'
# def confluent_kafka_producer_performance():
#     topic = 'confluent-kafka-topic'
#     conf = {'bootstrap.servers': bootstrap_servers}
#     producer = confluent_kafka.Producer(**conf)
#     messages_to_retry = 0
#
#     producer_start = time.time()
#     for i in range(msg_count):
#         try:
#             producer.produce('testBusdatac', value=msg_payload)
#         except BufferError as e:
#             messages_to_retry += 1
#
#     # hacky retry messages that over filled the local buffer
#     print(messages_to_retry)
#     for i in range(messages_to_retry):
#         producer.poll(0)
#         try:
#             producer.produce('testBusdatac', value=msg_payload)
#         except BufferError as e:
#             producer.poll(0)
#             producer.produce(topic, value=msg_payload)
#
#     producer.flush()
#
#     return time.time() - producer_start
#
# producer_timings['confluent_kafka_producer'] = confluent_kafka_producer_performance()
# calculate_thoughput(producer_timings['confluent_kafka_producer'])