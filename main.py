import requests
import lxml
import smtplib
from bs4 import BeautifulSoup
YOUR_SMTP_ADDRESS="smtp.gmail.com"
email = "ishita.kanpur29@gmail.com"
password = "Ishita@29$"



url = "https://www.amazon.com/dp/B08GC6PL3D/ref=sbl_dpx_B08GC6PL3D_0"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()

price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 187

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(email,password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
