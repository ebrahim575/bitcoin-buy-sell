# bitcoin-buy-sell

You need to implement the following code block into your existing python code you have that receives input from wherever and determines the buy or sell command.

So once that code determines buy or sell, you would want to pass that keyword "buy" or "sell" into the following

This code also only calls the btc-buy-sell.py file which does the actual html page of showing buy vs sell.
```
import os       # you will want to import these 2 modules at the top of that existing code
import signal

def run_script():
    # Get process id
    pid = os.getpid()
    
    # The resultFromOtherCode variable is the variable you have from the other code you have that determines whether the person is buying or selling
    command = "python3 btc-buy-sell.py " + resultFromOtherCode
    os.system(command)
    
    # Kill the command
    os.kill(pid, signal.SIGTERM)

run_script()
```
