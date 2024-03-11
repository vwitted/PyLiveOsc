from live import Set
import os
import mido
mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)
i=0
set.tracks
    print(f"{i}: {set.tracks[i].name}")
n = int(input("> "))
features = [x for x in dir(set.tracks[n]) if not x.startswith('_')]
for i in range(len(features)):
    print(f"{i}: {features[i]}")
m = int(input("> "))
pass
#dir( set.tracks[0].devices[0].parameters)
#[x.name for x in set.tracks[0].devices[0].parameters]