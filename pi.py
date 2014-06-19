from Pubnub import Pubnub
from iotconnector import iotbridge

pi = iotbridge(publish_key = 'demo', subscribe_key = 'demo', uuid = 'PI')

channel = 'button-reply'
message = "hello from pi"

# callback function for the user to play around with the received message
def callbackfn(message):
  print(message)

# Sending messages on the channel
pi.send(channel, message)

# Receiving messages on the channel
pi.connect(channel, callbackfn)
