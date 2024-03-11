from live import *

import logging

logging.basicConfig(format="%(asctime)-15s %(message)s")
logging.getLogger("live").setLevel(logging.INFO)

set = Set(scan=True)
set.dump() 