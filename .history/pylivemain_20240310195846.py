from live import Set
import os
# import mido
# mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)
print("Select Track")

for i in range(len(set.tracks)):
    print(f"{i}: {set.tracks[i].name}"
#dir( set.tracks[0].devices[0].parameters)
[x.name for x in set.tracks[0].devices[0].parameters]