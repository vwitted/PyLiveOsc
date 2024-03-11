from live import *

import mido
mido.set_backend("mido.backends.rtmidi")

set = Set(scan=True)
set.tracks[0].volume