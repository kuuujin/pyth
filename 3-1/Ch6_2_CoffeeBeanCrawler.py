from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

from selenium import webdriver
import time

#[CODE 1]
def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome()
    storeCnt = 0 
             
    for i in range(1, 10):  #마지막 매장번호(최근 신규 매장번호) 까지 반복
        wd.get(CoffeeBean_URL)
        time.sleep(1)  #웹페이지 연결할 동안 1초 대기
        try:
            wd.execute_script("storePop2(%d)" %i)
            time.sleep(1) #스크립트 실행 할 동안 1초 대기
            html = wd.page_source
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            result.append([str(i)]+[store_name]+[store_address]+[store_phone])
            print("%s %s" %(str(i), store_name))  #매장 이름 출력하기

            storeCnt += 1
        except:
            continue

    return storeCnt

#[CODE 0]
def main():
    result = []
    Cnt = 0

    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    Cnt = CoffeeBean_store(result)  #[CODE 1]
    print("총 매장 수 : %d" %Cnt)
    
    CB_tbl = pd.DataFrame(result, columns=('no', 'store', 'address','phone'))
    CB_tbl.to_csv('./CoffeeBean.csv', encoding='cp949', mode='w', index=True)

if __name__ == '__main__':
     main()
