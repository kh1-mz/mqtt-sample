"""Subscriber sample
"""
import paho.mqtt.client as mqtt

BROKER_HOST = 'localhost'
BROKER_PORT = 1883
TOPIC_PREFIX = 'paho/test/topic'


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    if reason_code_list[0].is_failure:
        print(f'Broker rejected you subscription: {reason_code_list[0]}')
    else:
        print('Broker granted the following QoS: {reason_code_list[0].value}')


def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connected with result code {reason_code}')
    client.subscribe(TOPIC_PREFIX)


def on_message(client, userdata, msg):
    print(f'{msg.topic} {msg.payload}')


def main():
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    
    mqttc.connect(BROKER_HOST, BROKER_PORT, 60)
    mqttc.loop_forever()


if __name__ == '__main__':
    main()
