import requests
import smtplib
from bs4 import BeautifulSoup

THRESHOLD_PRICE = 35
URL = f"https://www.amazon.it/Joma-Stagione-23-Maglia-Ufficiale-Bordeaux/dp/B09SG7ZWKL/ref=is_sr_dp_2?dib=eyJ2IjoiMSJ9.Sd0xz9e0y4nNULm02fDcvWbDWoFjN-PRU22sR5idsZVjGx7LFaFE47JQb22y2VVpgJPVXG4aCL9_qF-BIa5ieiz6GEvkU-YnEltKCTq6bBSMxOIA3R1oP0KpzdDHjhkVb1Q9bOegMQ80AvCtucK7W6HFenyFgWxd0-L6YZD6UQS9w5zY5hinFC4V3KtGLPeUQjBHVSfQVaG20_zNbtbg22djd3ges9i_qysXmWc43IwLU7R43TjEDLn42vyuJjoD6D3mwZO5yDgEwC2g6I8KxrVsovvXSaSQ3RTyLStilCI.w4UqSJvkW2_8ZkL6JfLDMqEZ4cg1pS8PtzEBe8aLZeU&dib_tag=se&keywords=maglia%2Btorino%2Bfc&qid=1725461719&sr=8-22&th=1"
SMTP_ADDRESS="smtp.gmail.com"
EMAIL_ADDRESS=""
EMAIL_PASSWORD=""


headers = {
    "User-Agent": "",
    "Accept-Language": ""
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()

price_without_currency = price.split("€")[0]
price_without_currency = price_without_currency.replace(",", ".")
price_as_float = float(price_without_currency)

subject = "Price Alert: Instant Pot Price Dropped!"
body = f"The price for the Instant Pot has dropped to € {price_as_float:.2f}!\nCheck it out here: {URL}"
msg = f"Subject: {subject}\n\n{body}"

if price_as_float < THRESHOLD_PRICE:

    subject = "Price Alert: Instant Pot Price Dropped!"
    body = f"The price for the Instant Pot has dropped to ${price_as_float:.2f}!\nCheck it out here: {URL}"
    msg = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(from_addr=SMTP_ADDRESS,
                            to_addrs=EMAIL_ADDRESS,
                            msg=msg)

    print("Email sent!")
else:
    print("No price drop detected.")


