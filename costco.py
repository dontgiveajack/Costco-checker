import time

from bs4 import BeautifulSoup
import requests
from twilio.rest import Client


def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll("img", {"class": "oos-overlay hide"})
    return len(out_of_stock_divs) != 0

def setup_twilio_client():
    account_sid = "XXXX"
    auth_token = "XXXX"
    return Client(account_sid, auth_token)

def send_notification():
    twilio_client = setup_twilio_client()
    twilio_client.messages.create(
        body="https://www.costco.ca/northrock-xcw-66-cm-%2826-in.%29-mountain-crossover-bike.product.100673608.html",
        from_="+ XXX",
        to="+XXX"
    )

def check_inventory():
    url = "https://www.costco.ca/northrock-xcw-66-cm-%2826-in.%29-mountain-crossover-bike.product.100673608.html"
    page_html = get_page_html(url)
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    if check_item_in_stock(page_html):
        send_notification()
        print("XCW In Stock")
    else:
        print(current_time)
       

while True:
    check_inventory()
    time.sleep(60)  # Wait a minute and try again