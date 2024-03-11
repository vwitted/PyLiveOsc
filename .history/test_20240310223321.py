import rtmidi
import mido
from rtmidi.midiconstants import CONTROL_CHANGE, NOTE_ON, NOTE_OFF, PITCH_BEND
midi_out = rtmidi.MidiOut()
available_ports = midi_out.get_ports()
print(available_ports)
midi_out.open_port(5)
midi_out.send_message([CONTROL_CHANGE, 60, 100])