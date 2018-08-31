import sys
import time

from paho.mqtt import client as mqtt_client

from constants import *


def mqtt_on_connect(client, userdata, flags, rc):
    # rc code expected => 0
    print("Connected with result code " + str(rc))
    client.subscribe(topic=TOPIC)
    print('Subscribed to {0}'.format(TOPIC))


def mqtt_on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    print('------------------')
    print('Incomming message')
    print('topic {0} | payload {1} | qos {2}'.format(message.topic, payload, message.qos))


def mqtt_log(client, userdata, level, buf):
    print('log: ', buf)


def main():
    # Client id must be unique.
    client = mqtt_client.Client('foo1')
    client.on_connect = mqtt_on_connect
    client.on_message = mqtt_on_message
    # client.on_log = mqtt_log
    client.connect(SERVER_IP)

    # client.loop_forever()
    client.loop_start()
    time.sleep(10)
    client.loop_stop()


if __name__ == '__main__':
    main()
    sys.exit(0)
