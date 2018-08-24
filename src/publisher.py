import sys

from paho.mqtt import publish as mqtt_publish

from constants import *


def mqtt_on_connect(client, userdata, flags, rc):
	print('Connected {0}'.format(client))


def main():
	mqtt_publish.single(
		topic=TOPIC,
		payload='hello there',
		qos=2,
		client_id='blob',
		hostname=SERVER_IP,
		port=SERVER_PORT)

if __name__ == '__main__':
	main()
	sys.exit(0)