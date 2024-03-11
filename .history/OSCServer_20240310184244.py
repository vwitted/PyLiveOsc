from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import math

from live import *
# import mido
# mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)

def filter_handler(address, *args):
    print(f"{address}: {args}")

def gyro_handler(address, *args):
    
    print(f"{address}: {args}")

def quat_handler(address, *args):
    set.tracks[0].volume = max(args[3],0)
    print(f"{address}: {args}")

dispatcher = Dispatcher()
dispatcher.map("/accelXYZ", filter_handler)
dispatcher.map("/GyroXYZ", gyro_handler)
dispatcher.map("/QuatIJKR", quat_handler)

ip = "0.0.0.0"
port = 1337


async def loop():
    """Example main loop that only runs for 10 iterations before finishing"""
    while True:
        await asyncio.sleep(1)


async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving

    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint


asyncio.run(init_main())