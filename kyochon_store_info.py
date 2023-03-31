from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
result = []
for page in range(1,18):
    for subpage in range(1,45):
        try:
            url= 'http://www.kyochon.com/shop/domestic.asp'
            kyochon_url = url+'?sido1='+ str(page) + '&sido2='+ str(subpage)
            html = urllib.request.urlopen(kyochon_url)
            soupkyochon = BeautifulSoup(html, 'html.parser')
            tag_div = soupkyochon.find("div", {"class": "shopSchList"})
            tag_a = tag_div.find_all('a')
            for store in tag_a:
                store_name = store.find('strong').string
                store_address = store.find('em').get_text().strip().split('\r')[0]
                store_sido = store_address.split()[0]
                store_gungu = store_address.split()[1]
                result.append([store_name] + [store_sido] + [store_gungu] + [store_address])
        except:
            pass
kyochon_tbl = pd.DataFrame(result, columns=('store', 'sido','gungu', 'address'))
kyochon_tbl.to_csv('C:/Users/User/Desktop/kyochon/kyochon.csv',encoding = "cp949", mode = "w", index = True)