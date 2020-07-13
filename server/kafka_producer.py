import confluent_kafka
import os
import json
from datetime import datetime
import uuid
import time


class Producers(object):

    def __init__(self):
        self.bootstrap_servers = os.environ.get('bootstrap_servers')
        self.topic = os.environ.get('topicname')


    def get_producer_file_path(self, id):
        return 'server/data/bus' + str(id) + '.json'

    def generate_bus_line(self, id):
        return 'SS07' + str(id)

    def get_coordinates(self, path):
        with open(path) as f:
            data = json.load(f)
        return data['features'][0]['geometry']['coordinates']

    def generate(self, coordinates, busline):
        conf = {'bootstrap.servers': self.bootstrap_servers}
        producer = confluent_kafka.Producer(**conf)
        message_data = {'busline': busline}
        i = 0
        while i < len(coordinates):
            try:
                message_data['key'] = message_data['busline'] + "_" + str(uuid.uuid4().hex)
                message_data['timestamp'] = str(datetime.utcnow())
                message_data['lat'] = coordinates[i][1]
                message_data['long'] = coordinates[i][0]
                message = json.dumps(message_data).encode()

                producer.produce(self.topic, value=message)

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
                    topic=self.topic,
                    value=message,
                )

    def start_producer(self, producer_id):

        data_file_path = self.get_producer_file_path(id=producer_id)

        coordinates = self.get_coordinates(path=data_file_path)

        busline = self.generate_bus_line(id=producer_id)

        self.generate(coordinates=coordinates, busline=busline)
