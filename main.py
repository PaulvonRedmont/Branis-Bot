import requests
import time
import finnhub


FINNHUB_API_KEY = ''  # Replace with your actual API key
STOCK_SYMBOL = 'AAPL'  # Replace with the stock symbol you want to track

def get_stock_price():
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
    quote = finnhub_client.quote(STOCK_SYMBOL)
    return STOCK_SYMBOL, quote['c']  # 'c' is the current price


def send_stock_price_message(webhook_url, stock_symbol, stock_price):
    message_content = f"Stock Price Update\nSymbol: {stock_symbol}\nPrice: {stock_price}"

    payload = {'content': message_content}
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Replace 'your_webhook_url' with the actual webhook URL obtained from Discord
webhook_url = ''

x = True

while x:
    stock_symbol, stock_price = get_stock_price()
    send_stock_price_message(webhook_url, stock_symbol, stock_price)
    time.sleep(60)
