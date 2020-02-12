import time

from chronometer import Chronometer

a = Chronometer()
a.start()
time.sleep(1)
a.stop()
a.start()
time.sleep(2)
a.stop()
print(a)
print("time should be around 3 seconds")
