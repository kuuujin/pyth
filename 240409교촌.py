from bs4 import BeautifulSoup
import urllib.request
import datetime
import json
import pandas as pd


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
        for sido2 in count():
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

    for i in range(1000//5):
        jsonData = getPage(i*5 +1)
        if(jsonData['ChunmanFreeSuggestions']['RESULT']['CODE'] == 'INFO-100'):
            print('인증키 오류')
            return
    
        if(jsonData['ChunmanFreeSuggestions']['RESULT']['CODE'] == 'INFO-000'):
            for i in range(5):
                SN = jsonData['ChunmanFreeSuggestions']['row'][i]['SN']
                TITLE = jsonData['ChunmanFreeSuggestions']['row'][i]['TITLE']
                CONTENT_link = jsonData['ChunmanFreeSuggestions']['row'][i]['CONTENT']
                VOTE_SCORE = jsonData['ChunmanFreeSuggestions']['row'][i]['VOTE_SCORE']
                DATE = jsonData['ChunmanFreeSuggestions']['row'][i]['REG_DATE']
                result.append([SN, TITLE, CONTENT_link, VOTE_SCORE, DATE])
    
    print('총 건수 : %s' %jsonData['ChunmanFreeSuggestions']['list_total_count'])
    return result
    

def main():
    jsonResult = []
    result = []

    print("<< 상상대로 서울 자유제안 정보 데이터를 수집합니다 >>")
    
    result = getItemAll()
    columns = ['SN', 'TITLE', 'CONTENT_link', 'VOTE_SCORE', 'DATE']
    result_df = pd.DataFrame(result, columns= columns)
    result_df.to_csv('상상대로서울자유제안.csv', index=False, encoding='cp949')

if __name__ == '__main__':
    main()