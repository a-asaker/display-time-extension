#!/usr/bin/env python3
# Coded By : A_Asaker

import time,threading,sys

def terminal_time():
 while 1:
  time.sleep(.1)
  print("\0337 \033[H\033[2K\t\t\t\033[1;4;41m" + time.asctime(time.localtime())+"\033[0m \0338",end="")
  sys.stdout.flush()
threading.Thread(target=terminal_time,daemon=True).start()

#Your Program Is Here ..
#   Some Code ....
#   Some Code ....
#   Some Code ....

# Ex:
x=input(">>> ")
