# bitcoin-buy-sell
you need to implement the following logic into the already exitsting python code you said you have in regards to a python script that received input for buy and sell commands.

import os
import signal

# Run a command
pid = os.getpid()
os.system("python3 btc-buy-sell.py sell")

# Kill the command
os.kill(pid, signal.SIGTERM)

so if the signal from the sensor is buy, the python script you already have needs to call this. if u need help lmk. so if buy command do all this but with buy instead of sell at end.
