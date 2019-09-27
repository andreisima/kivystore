import json
from kivy.clock import mainthread
import paho.mqtt.client as mqtt
from store.manager import Manager


class MessageService (Manager):

    def __init__(self, **kwargs):

        # mqtt setup
        brokerIP = '10.0.1.90'
        brokerPort = 1883
        client = mqtt.Client(clean_session=True)

        def onConnect(client, userdata, flags, rc):
            print(f'Message Serv: Connected with code: {str(rc)}')

        def onDisconnect(client, userdata, message):
            print(f'Message Serv: Disconnected from broker')

        def onSubscribe(client, userdata, mid, granted_qos):
            print(f'Message Serv: Subscribed to topic')

        def onUnsubscribe(client, userdata, mid, granted_qos):
            print(f'Message Serv: Unsubscribed from topic')

        def onMessage(client, userdata, message):
            msg = message.payload.decode('utf-8')
            data = json.loads(msg)
            self.msg_router(message.topic, data)
        client.on_connect = onConnect
        client.on_disconnect = onDisconnect
        client.on_subscribe = onSubscribe
        client.on_unsubscribe = onUnsubscribe
        client.on_message = onMessage

        # try if connection
        client.connect(brokerIP, brokerPort, keepalive=60, bind_address='')
        client.loop_start()
        client.subscribe('app/ui/switch')
        client.subscribe('app/ui/sensor')

    @mainthread
    def msg_router(self, topic, data):
        store_ref = topic.split('/')
        store_ref = store_ref[-1] + '_manager'
        if store_ref in self.manager.val:
            instance = self.manager.val[store_ref]
            instance.update_object(
                uuid=data['uuid'],
                value=data['value'],
                updated_at=data['upddated_at']

            )
        else:
            print(f'no instance with key:{store_ref}')
