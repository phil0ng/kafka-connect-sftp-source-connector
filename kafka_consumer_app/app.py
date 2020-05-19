"""
This module is a consumer application that will consume messages
from a kafka topic and post to 0.0.0.0:5001 in real time
"""

import os
import time
from flask import Flask, render_template, Response
from pykafka import KafkaClient


time.sleep(30)

app = Flask(__name__)

topic_name = os.environ.get('KAFKA_TOPIC')
kafka_host = os.environ.get('KAFKA_HOST')

client = KafkaClient(hosts=kafka_host)

@app.route('/kafka/getmessages')
def get_consumer():
    """Get messages from kafka topic"""
    def events():
        for i in client.topics[topic_name].get_simple_consumer():
            yield 'message:{0}\n\n'.format(i.value.decode())

    return Response(events(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
