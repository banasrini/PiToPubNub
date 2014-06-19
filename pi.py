from Pubnub import Pubnub
from iotconnector import iotbridge
 
pi = iotbridge(publish_key = 'demo', subscribe_key = 'demo', uuid = 'PI')
 
channel = 'iotchannel'
message = "hello from pi"
 
def callbackfn(message):
  print(message)
 
pi.send(channel, message)
pi.connect(channel, callbackfn)
