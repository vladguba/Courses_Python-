import os
import bs4
import requests

site_url = "https://cland.if.ua/product-category/noutbuky-ta-planshety/elektronni-knygy/"

with open("site.csv", "w") as f:

    main_page = requests.get(site_url)
    main_page_bs = bs4.BeautifulSoup(main_page.text, "html.parser")
    goods = main_page_bs.find_all('div', {'class': 'product-entry'})

    for num, content in enumerate(goods):
        print('\n*************************')
        text = ''
        title = goods[num].find('h3')
        title_l = title.get_text().strip()
        print(title_l)
        text += '\"' + title_l + '\",'

        prices = goods[num].find_all('span', {'class': 'price'})
        for price in prices:
            value = price.find('span', {'class': 'woocommerce-Price-amount amount'})
            print(value.get_text().strip())
            text += value.get_text().strip()

        image = goods[num].find('div', {'class': 'over-img'})
        print(image.img['src'])
        img_url = image.img['src']
        data = requests.get(img_url, stream=True)
        base = os.path.dirname(__file__)
        file_name = base + '/' + "img/" + title_l + ".jpg"
        with open(file_name, "bw") as f_image:
            f_image.write(data.content)

        text += file_name
        print(text)
        f.write(text + "\n")

        print('*************************')



