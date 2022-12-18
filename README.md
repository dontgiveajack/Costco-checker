# Costco in-stock checker
Checks if an item on Costco is in stock and get notified (requires twilio)

## How to use:

Run the monitor.py script which watches the other script if it crashes due to the product being removed from costco periodically (ie: if the URL returns a 404, the script crashes. So you'll wan to restart it). Monitor.py will restart the script:

example: `python3 monitor.py costco.py`

