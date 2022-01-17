from requests_html import HTMLSession

session = HTMLSession()

url = 'https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99'

r = session.get(url)

r.html.render(sleep=2, keep_page=True, scrolldown=1)

app = r.html.find('.product-actions')

for item in app:
    title = {
        "name": item,
        # "price": Double,
        # "color": String,
        # "size": Array
    }
    print(title)
