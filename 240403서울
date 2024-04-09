import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd

ServiceKey = "64517a4864726277353076526d6457"

#[CODE 1]
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
    
#[CODE 2]
def getPage(start):
    service_url = 'http://openAPI.seoul.go.kr:8088/' + ServiceKey + '/json/ChunmanFreeSuggestions/%d/%d/' %(start, start+5)
    retData = getRequestUrl(service_url) #[CODE 1]

    if (retData == None):
        return None
    else:
        return json.loads(retData)

#[CODE 3]    
def getItemAll():
    
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
    result_df.to_csv('/상상대로서울자유제안.csv', index=False, encoding='cp949')

if __name__ == '__main__':
    main()