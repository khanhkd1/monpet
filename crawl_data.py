from operator import le
import requests
import random
from bs4 import BeautifulSoup
from lxml import etree, html


# from store.models import Category, Product, Image

def get_data_save_db(category_model=None, product_model=None, image_model=None):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    urls = ['https://digione.vn/camera-ezviz-trong-nha/', 'https://digione.vn/camera-ezviz-ngoai-troi/']
    category = ['Camera Ezviz trong nhà', 'Camera Ezviz ngoài trời']

    data = []

    for i in range(len(urls)):
        req = requests.get(urls[i], headers=headers)
        soup = BeautifulSoup(req.content, "html.parser")
        ul_images = soup.find('ul', id="list-product-all")
        figures = ul_images.find_all('figure')

        data.append({
            'category': category[i],
            'product': []
        })

        for figure in figures:
            data[i]['product'].append({
                'product_url': f"https://digione.vn/{figure.find('a').get('href')}"
            })

    for i in range(len(data)):
        for j in range(len(data[i]['product'])):
            req = requests.get(data[i]['product'][j]['product_url'], headers=headers)
            soup = BeautifulSoup(req.content, "html.parser")
            dom = etree.HTML(str(soup))

            data[i]['product'][j]['title'] = dom.xpath('/html/body/section[2]/div/div[1]/h1/a')[0].text.strip()
            data[i]['product'][j]['price'] = int(dom.xpath('/html/body/section[2]/div/div[3]/div[2]/div[1]/p[1]/span[2]/text()')[0].replace('.', ''))
            data[i]['product'][j]['avaiable'] = bool(random.getrandbits(1))
            data[i]['product'][j]['description'] = ''
            data[i]['product'][j]['image_urls'] = []

            li_contents = dom.xpath('//div[@class="product_info_special_content"]')[0].xpath('.//li')
            
            for k in range(len(li_contents)):
                if li_contents[k].xpath('.//strong/text()'):
                    data[i]['product'][j]['description'] += f"{li_contents[k].text}{li_contents[k].xpath('.//strong/text()')[0]}\n"
                else:
                    data[i]['product'][j]['description'] += f"{li_contents[k].text}\n"
            
            image_urls = dom.xpath('//ul[@class="main-list-product-image"]')[0].xpath('.//li')
            for k in range(len(image_urls)):
                data[i]['product'][j]['image_urls'].append(image_urls[k].xpath('.//img')[0].get('data-src'))
    
    # save data
    for i in range(len(data)):
        category = category_model(title=data[i]['category'])
        category.save()

        for j in range(len(data[i]['product'])):
            product = product_model(category_id=category, title=data[i]['product'][j]['title'], \
                price=data[i]['product'][j]['price'], avaiable=data[i]['product'][j]['avaiable'], \
                    description=data[i]['product'][j]['description'])
            product.save()

            for k in range(len(data[i]['product'][j]['image_urls'])):
                image = image_model(product_id=product, image_url=data[i]['product'][j]['image_urls'][k])
                image.save()
