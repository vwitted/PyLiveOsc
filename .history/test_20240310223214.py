import rtmidi
import mido
from rtmidi.midiconstants import C
midi_out = rtmidi.MidiOut()
available_ports = midi_out.get_ports()
print(available_ports)
midi_out.open_port(5)
midi_out.send_message(mido.Message('cc', channel=0, value=66))