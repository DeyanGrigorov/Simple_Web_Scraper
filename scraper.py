import json

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99')
results = {}
content = driver.page_source
soup = BeautifulSoup(content, 'lxml')
driver.quit()

for element in soup.findAll(attrs={'product-features'}):
    name = element.find('h1')
    results['name'] = name.text

for element in soup.findAll(attrs='colors-info'):
    color = element.find(attrs='colors-info-name')
    results['color'] = color.text

for element in soup.findAll(attrs='product-prices'):
    price = element.find('meta', attrs={'itemprop': 'price'})
    results['price'] = price['content']

for element in soup.findAll(attrs='selector-list'):
    spans = soup.find_all('span', {'class': 'size-unavailable'})
    lines = [span.get_text() for span in spans]
    if lines:
        results['unavailable sizes'] = lines
    else:
        results['unavailable sizes'] = 'Everything is available'

for element in soup.findAll(attrs='selector-list'):
    spans = soup.find_all('span', {'class': 'size-available'})
    lines = [span.get_text() for span in spans]
    if bool(lines):
        results['available sizes'] = lines
    else:
        results['available sizes'] = 'Everything is unavailable'

json_object = json.dumps(results)

print(json_object)
