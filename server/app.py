from flask import Flask, render_template, Response
from flask_cors import CORS, cross_origin
import confluent_kafka
import uuid
import json
import os
from config_loader import load_config

# load configs
load_config()

app = Flask(__name__)
CORS(app)



app.config['DEBUG'] = os.environ.get('debugger')
@app.route('/')
def index():
    return(render_template('index.html'))

#Consumer API
@app.route('/topic/<topicname>')
def get_messages(topicname):
    def events():
        bootstrap_servers = os.environ.get('bootstrap_servers')
        conf = {'bootstrap.servers': bootstrap_servers,
                'session.timeout.ms': 6000,
                'group.id': uuid.uuid1(),
                'default.topic.config': {'auto.offset.reset': 'latest'}
                }
        consumer = confluent_kafka.Consumer(**conf)

        consumer.subscribe([topicname])
        while True:
            msg = consumer.poll(1)
            if msg is None:
                continue
            elif not msg.error():

                yield 'data:{0}\n\n'.format(msg.value().decode())

    return Response(events(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, port=8081)
