# bitcoin-buy-sell

You need to implement the following code block into your existing python code you have that receives input from wherever and determines the buy or sell command.

So once that code determines buy or sell, you would want to pass that keyword "buy" or "sell" into the following

This code also only calls the btc-buy-sell.py file which does the actual html page of showing buy vs sell.
```
import os       # you will want to import these 2 modules at the top of that existing code
import signal

resultFromOtherCode = 'buy'
# Get process id
pid = os.getpid()

# The resultFromOtherCode variable is the variable you have from the other code you have that determines whether the person is buying or selling
command = "python3 btc-buy-sell.py " + resultFromOtherCode
os.system(command)

# Kill the command
os.kill(pid, signal.SIGTERM)
```
Note this code assumes that you have a working code that determines whether you want to buy or sell. It also assumes that you will place the following files in the same directory as the existing code that determines buy vs sell.
- btc-buy-sell.py
- execute_command_os.py
- bitcoin_count.txt

Also this assumes that you are running this on mac and that your python name is 'python3' and no 'py'
To change it to py and windows you will want to do the following.
- Change the ```os.system("python3 btc-buy-sell.py sell")``` to ```os.system("py btc-buy-sell.py sell")```


- Change the ```chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'``` to ```chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'``` in the btc-buy-sell.py file.
