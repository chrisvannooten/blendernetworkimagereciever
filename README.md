# Blender Network Reciever

### Usage

Unlike the [head addon](https://github.com/chrisvannooten/blenderimagenetworkrender) you don't need to setup much, simply enable the addon and you are good to go.
It starts up a Python thread and Socket through the init script, the thread is a daemon so it shuts
down if blender shuts down. However unregistring the addon will not, it is adviced to unregister the addon and then restart Blender if you want to shut it down.
