from Pubnub import Pubnub
import string
import time
import random
import uuid
 
 
 
class iotbridge(object):
    def __init__(self, publish_key,
        subscribe_key,uuid):
 
        self.publish_key = publish_key
        self.subscribe_key = subscribe_key
        self.uuid = uuid
        self.pubnub = Pubnub( 'demo', 'demo', None, False)
        self.pubnub.uuid = self.uuid
    
    
    
    def send(self, channel, message):
        # Sending message on the channel
        self.pubnub.publish({
            'channel' : channel,
            'message' : message})
 
    def connect(self, channel, receiver):
        # Listening for messages on the channel
        self.pubnub.subscribe({
            'channel' : channel,
            'callback' : receiver
        })
