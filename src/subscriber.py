import sys

from paho.mqtt import client as mqtt_client

from constants import *


def mqtt_on_connect(client, userdata, flags, rc):
	print('Connected {0}'.format(client))
	client.subscribe(topic=TOPIC, qos=2)
	print('Subscribed to {0}'.format(TOPIC))


def mqtt_on_message(client, userdata, message):
	print('------------------')
	print('Incomming message')
	print('topic {0} | payload {1} | qos {2}'.format(message.topic, message.payload, message.qos))


def main():
	client = mqtt_client.Client(client_id='blob')
	client.on_connect = mqtt_on_connect
	client.on_message = mqtt_on_message
	client.connect(host=SERVER_IP, port=SERVER_PORT, 60)
	client.loop_forever()


if __name__ == '__main__':
	main()
	sys.exit(0)