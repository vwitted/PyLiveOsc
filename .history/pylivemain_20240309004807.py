from live import classes
# import mido
# mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)
dir( set.tracks[0].devices[0].parameters)
[x.name for x in set.tracks[0].devices[0].parameters]
classes.