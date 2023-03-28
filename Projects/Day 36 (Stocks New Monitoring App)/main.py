from StockAPI import StockAPI
from NewsAPI import NewsAPI
from twilio.rest import Client
import os

STOCK = "IBM"
COMPANY_NAME = "IBM"

# Get stock percentage change from StockAPI
ibm_stock = StockAPI(STOCK)

# Get the latest article with the company name in title, in english
ibm_news = NewsAPI(COMPANY_NAME)

# Send sms message through twilio
account_sid = "ACea3c49fae83e4c51d11160d369877b85"
auth_token = os.environ.get("TWILIO_API")

sms_text = f"\n{STOCK}: {ibm_stock.percentage_change:.2f}%\n" \
           f"Headline: {ibm_news.latest_article['title']}\n" \
           f"Brief: {ibm_news.latest_article['description']}"

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=sms_text,
    from_="+14406364934",
    to="+5511964922298"
)
print(message.status)
print(sms_text)

