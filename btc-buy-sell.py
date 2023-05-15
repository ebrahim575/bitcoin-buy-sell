import webbrowser
import argparse
import os

# Define the file path to store the Bitcoin count
file_path = "bitcoin_count.txt"

# Read the current Bitcoin count from the file, or initialize it to 0
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        bitcoin_count = int(f.read())
else:
    bitcoin_count = 0

# Parse the command-line argument
parser = argparse.ArgumentParser(description='Update the Bitcoin counter.')
parser.add_argument('action', type=str, help='the action to perform: "buy" or "sell"')
args = parser.parse_args()

# Define the emoji and color for the HTML page based on the command-line argument
if args.action == "buy":
    emoji = "🎉"
    color = "success"
    bitcoin_count+=1
    buy_sell_text = "Bought"

elif args.action == "sell":
    emoji = "😢"
    color = "danger"
    bitcoin_count-=1
    buy_sell_text = "Sold"


    # Limit the minimum Bitcoin count to 0 when selling


# Update the HTML content to display the updated Bitcoin count and emoji
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bitcoin Counter</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZEZI7hKXQ9WO+gSwB4jwB" crossorigin="anonymous">
</head>
<body style="background: yellow;" class="d-flex align-items-center justify-content-center">
    <div class="container py-5">
        <div class="row">
            <div class="col-md-8 mx-auto">
                <div class="card" style="min-height: 100vh;">
                    <div class="card-body text-center">
                        <h1 style="font-size: 5rem;" class="display-1 text-center">Detected <br> {buy_sell_text} 1 bitcoin<br>Total : {bitcoin_count} bitcoin {emoji}</h1>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>

"""



# Register the Chrome browser with the webbrowser module
chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open the updated HTML content in Chrome
url = f"data:text/html,{html_content}"
webbrowser.get('chrome').open(url)

# Write the updated Bitcoin count to the file
with open(file_path, "w") as f:
    f.write(str(bitcoin_count))
