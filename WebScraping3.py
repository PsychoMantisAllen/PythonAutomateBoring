import bs4
import requests

res = requests.get('https://www.amazon.com.au/Automate-Boring-Stuff-Python-Sweigart/dp/1593275994')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
# CSS selector, find the element you want and right click copy selector
elems = soup.select('#unqualified-buybox-olp > div > span')

print(elems)

print(elems[0].text)
print(elems[0].text.strip())    # strip() gets rid of the empty space

def getamazonprice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#unqualified-buybox-olp > div > span')
    return elems[0].text.strip()


price = getamazonprice('https://www.amazon.com.au/Automate-Boring-Stuff-Python-Sweigart/dp/1593275994')
print('The price is ' + price)