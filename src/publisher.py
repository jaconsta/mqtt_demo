import sys

from paho.mqtt import publish as mqtt_publish
from paho.mqtt import client as mqtt_client

from constants import *


def mqtt_on_connect(client, userdata, flags, rc):
    print('Connected {0}'.format(client))


def mqtt_log(client, userdata, level, buf):
    print('log: ', buf)


def first_way():
    client = mqtt_client.Client('foo2')
    client.on_log = mqtt_log
    client.connect(SERVER_IP)
    client.publish(TOPIC, 'bar')


def second_way():
    mqtt_publish.single(
        topic=TOPIC,
        payload='Message 2',
        hostname=SERVER_IP,
        port=SERVER_PORT,
        client_id='foo3'
    )


def main():
    first_way()
    second_way()


if __name__ == '__main__':
    main()
    sys.exit(0)
