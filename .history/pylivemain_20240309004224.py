from live import *
# import mido
# mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)
dir()
[x.name for x in set.tracks[0].devices[0].parameters]