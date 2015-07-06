from pubnub import Pubnub
from iotconnector import iotbridge
 
pi = iotbridge(publish_key = 'demo', subscribe_key = 'demo', uuid = 'PI')
 
channel = 'iotchannel'
message = "hello from pi"
 
def callbackfn(m, n):
  print(m)
 
pi.send(channel, message)
pi.connect(channel, callbackfn)
