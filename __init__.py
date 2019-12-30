bl_info = {
    "name":"Network Render Reciever",
    "description":"The reciever for the Network Render Sender",
    "blender":(2,80,0),
    "category":"All"
}

import bpy
import socket
from .renderserver import RenderThread

def register():
    socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket1.bind(('',65432))
    socket1.listen()
    mythread = RenderThread(1,'Server Render Thread',socket1,'/tmp/incoming.blend')
    mythread.daemon = True
    mythread.start()


def unregister():
    print("Unregistering Network Render Reciever")
