import os
import signal

resultFromOtherCode = 'sell'
# Get process id
pid = os.getpid()

# The resultFromOtherCode variable is the variable you have from the other code you have that determines whether the person is buying or selling
command = "python3 btc-buy-sell.py " + resultFromOtherCode
os.system(command)

# Kill the command
os.kill(pid, signal.SIGTERM)


