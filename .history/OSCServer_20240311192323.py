from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
from DynamicScaling import *
import rtmidi
from rtmidi.midiconstants import CONTROL_CHANGE, NOTE_ON, NOTE_OFF, PITCH_BEND

from live import *
# import mido
# mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)
ACCEL=False
GYRO=True
QUAT=True

midi_out = rtmidi.MidiOut()
available_ports = midi_out.get_ports()
print(available_ports)
midi_out.open_port(5)
GyroScaler=DynamicScaler()
AccelScaler=DynamicScaler()
QuatScaler=DynamicScaler()

def setAccelX():
    midi_out.send_message([CONTROL_CHANGE, 60, 50])

def setAccelY():
    midi_out.send_message([CONTROL_CHANGE, 61, 50])

def setAccelZ():
    midi_out.send_message([CONTROL_CHANGE, 62, 50])

def setGyroX():
    midi_out.send_message([CONTROL_CHANGE, 63, 50])

def setGyroY():
    midi_out.send_message([CONTROL_CHANGE, 64, 50])

def setGyroZ():
    midi_out.send_message([CONTROL_CHANGE, 65, 50])
input()
setGyroX()

setGyroY()

def accel_handler(address, *args):
    if ACCEL:
        [AccelScaler.update_range(x) for x in args]
        args=[AccelScaler.scale(x) for x in args]
        midi_out.send_message([CONTROL_CHANGE, 60, args[0]])
        midi_out.send_message([CONTROL_CHANGE, 61, args[1]])
        midi_out.send_message([CONTROL_CHANGE, 62, args[2]])
        print(f"{address}: {args}")

def gyro_handler(address, *args):
    if GYRO:
        [GyroScaler.update_range(x) for x in args]
        args=[GyroScaler.scale(x) for x in args]
        midi_out.send_message([CONTROL_CHANGE, 63, args[0]])
        midi_out.send_message([CONTROL_CHANGE, 64, args[1]])
        midi_out.send_message([CONTROL_CHANGE, 65, args[2]])
        print(f"{address}: {args}")

def quat_handler(address, *args):
    if QUAT:
        [QuatScaler.update_range(x) for x in args]
        args=[QuatScaler.scale(x) for x in args]
        midi_out.send_message([CONTROL_CHANGE, 66, args[0]])
        midi_out.send_message([CONTROL_CHANGE, 67, args[1]])
        midi_out.send_message([CONTROL_CHANGE, 68, args[2]])
        midi_out.send_message([CONTROL_CHANGE, 69, args[3]])

dispatcher = Dispatcher()
dispatcher.map("/accelXYZ", accel_handler)
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