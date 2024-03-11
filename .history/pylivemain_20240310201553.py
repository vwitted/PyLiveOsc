from live import Set
import os
# import mido
# mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)
print("Select Track")

for i in range(len(set.tracks)):
    print(f"{i}: {set.tracks[i].name}")
n = int(input("> "))
features = [x for x in dir(set.tracks[n]) if x.startswith('_')]
for i in range(lendir(set.tracks[n]))):
    print(f"{i}: {dir(set.tracks[n])[i]}")
m = int(input("> "))
#dir( set.tracks[0].devices[0].parameters)
#[x.name for x in set.tracks[0].devices[0].parameters]