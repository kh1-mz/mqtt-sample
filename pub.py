"""Publisher sample
"""
import time
import paho.mqtt.client as mqtt


BROKER_HOST = 'localhost'
BROKER_PORT = 1883
TOPIC = 'paho/test/topic'


def on_publish(client, userdata, mid, reason_code, properties):
    try:
        userdata.remove(mid)
    except KeyError:
        print('ERROR')


def main():
    unacked_publish = set()

    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_publish = on_publish
    mqttc.user_data_set(unacked_publish)

    mqttc.connect(BROKER_HOST, BROKER_PORT, 60)
    mqttc.loop_start()

    msg_info = mqttc.publish(TOPIC, 'my message', qos=1)
    unacked_publish.add(msg_info.mid)

    msg_info2 = mqttc.publish(TOPIC, 'my message2', qos=1)
    unacked_publish.add(msg_info2.mid)

    msg_info3 = mqttc.publish(TOPIC, 'my message3', qos=1)
    unacked_publish.add(msg_info3.mid)

    while len(unacked_publish):
        time.sleep(0.1)

    msg_info.wait_for_publish()
    msg_info2.wait_for_publish()

    mqttc.disconnect()
    mqttc.loop_stop()


if __name__ == '__main__':
    main()
