from live import *
# import mido
# mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)
print(set.tracks[0].devices[0].get_parameter(1))