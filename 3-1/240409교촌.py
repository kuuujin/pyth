from bs4 import BeautifulSoup
import urllib.request
import datetime
import pandas as pd
from itertools import count



#[CODE 1]
def getRequestUrl(url, enc='utf-8'):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')
            
            return ret
    
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
    
#[CODE 2]
def getKyochonAddress(result):

    for sido1 in range(1, 18):
        for sido2 in count(1):
            Kyochon_URL = 'https://www.kyochon.com/shop/domestic.asp?sido1=%s&sido2=%s&txtsearch=' %(str(sido1), str(sido2))
            print(Kyochon_URL)

            try:
                rcv_data = getRequestUrl(Kyochon_URL)
                soupData = BeautifulSoup(rcv_data, 'html.parser')

                ul_tag = soupData.find('ul', attrs={'class': 'list'})

                for store_data in ul_tag.findAll('a', href=True):
                    store_name = store_data.find('strong').get_text()
                    store_address = store_data.find('em').get_text().strip().split('\r')[0]
                    store_phone = store_data.find('em').get_text().strip().split('\r')[2].strip()
                    store_sido_gu = store_address.split()[:2]
                    store_sido_gu1 = '%s %s' %(store_sido_gu[0], store_sido_gu[1])
                    result.append([store_name] + [store_sido_gu1] + [store_address] + [store_phone])
            except:
                break
    
    return

#[CODE 3]    
def cswin_Kyochon():
    
    result = []

    print('교촌 주소 크롤링')
    getKyochonAddress(result)

    kyochon_table = pd.DataFrame(result, columns=('store', 'sido_gungu', 'store_address', 'store_phone'))
    kyochon_table.to_csv("kyochon.csv",encoding='cp949', mode='w', index=True)
    del result[:]

    print('끝')
    


if __name__ == '__main__':
    cswin_Kyochon()