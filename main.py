import os
import signal

# Run a command
pid = os.getpid()
os.system("python3 btc-buy-sell.py sell")

# Kill the command
os.kill(pid, signal.SIGTERM)
