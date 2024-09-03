from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

#[CODE 1]
def hollys_store(result):
    for page in range(1,59):
        i = 0
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store=' %page

        html = urllib.request.urlopen(Hollys_url)
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody')
        for store in tag_tbody.find_all('tr'):
            if len(store) <= 3:
                break
            
            store_td = store.find_all('td')
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            i += 1
            no = "{0:0>3}-{1:0>3}".format(str(page), str(i))
            result.append([store_name]+[store_sido]+[store_address]+[store_phone]+[no])

        print(Hollys_url, no)
    return

#CODE 0]
def main():
    result = []
    print('Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    hollys_store(result)   #[CODE 1] 호출
    print(len(result))
    print(result[0])
    print(result[(len(result) -1)])
    
    hollys_tbl = pd.DataFrame(result, columns=('store', 'sido-gu', 'address','phone', 'no'))
    hollys_tbl.to_csv('hollys.csv', encoding='cp949', mode='w', index=True)
    del result[:]
       
if __name__ == '__main__':
     main()
