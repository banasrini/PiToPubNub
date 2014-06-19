PiToPubNub
==========
For those of you who use it, you know just how powerful the Raspberry Pi is. It is smaller than your palm, but can double up as your PC and is infact even more capable than our regular computers when it comes to reading the environment around us. The Pi can be used to control other devices as well as collect information from them. What better way to jump into the IoT space if not through the powerful Pi. Using PubNub's real time global network and the capabilities of the Pi, the applications are countless. 

Here, I have demonstrated how to connect the Raspberry Pi to the PubNub network with less than 10 lines of code. I have used Python, but feel free to use any SDK to run on the Raspberry Pi. PubNub offers around 50 SDKs for you to use.

To see this in action locally, clone the source from Github and run the Python script from the command line.


Two Simple Commands
======

The code is so simple and straightforward. 
```python
from Pubnub import Pubnub
from iotconnector import iotbridge

pi = iotbridge(publish_key = 'demo', subscribe_key = 'demo', uuid = 'PI')

channel = 'button-reply'
message = "hello from pi"

def callbackfn(message):
  print(message)

pi.send(channel, message)
pi.connect(channel, callbackfn)

```
Create an instance of the iotwrapper called pi. Initialize all the variables such as publish key, subscribe key, channel and message. These are necessary for connecting to the PubNub network.

```python
pi.send(channel, message) 
```
This method lets you connect to the PubNub global network by calling the publish method internally. This takes in channel, as in the channel we want to publish to and the message to be sent on it.

```python
pi.connect(channel,callbackfn)
```

This method lets you subscribe to a particular channel. So if you want to receive messages from another Pi or device on the PubNub network, just subscribe to the channel that they are publishing on. 
The callbackfn - callback function, will let you consume the message that you receive. So you can either print it, or store it or send it to someone else. We let that up to you. 

It cannot get simpler than this. Copy paste the above code and start connecting. 
