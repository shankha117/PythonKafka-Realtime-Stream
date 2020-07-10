
import json
from datetime import datetime
import uuid

# read the coordinates from file
with open('./data/bus2.json') as f:
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
message_data['busline'] = '00002'

import time
def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):
        message_data['key'] = message_data['busline'] + "_" + str(uuid.uuid4().hex)
        message_data['timestamp'] = str(datetime.utcnow())
        message_data['lat'] = coordinates[i][1]
        message_data['long'] = coordinates[i][0]

        producer.produce(topic, value=json.dumps(message_data).encode())

        time.sleep(0.5)

        print(message_data)

        if i == len(coordinates) - 1:
            i = 0
        else:
            i += 1


generate_checkpoint(coordinates)
