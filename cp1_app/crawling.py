import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import sqlite3

#지원 관련 정보 api로 불러와 데이터프레임으로 반환하는 함수
#정책자금: found
#성장지원: grow
#재기지원: comeback
#창업지원: startup
#전통시장활성화: market
#보증지원: grnty
def policy_info(query):
    #get
    policy_link=requests.get(f'https://www.sbiz.or.kr/sup/policy/json/policy{query}.do')
    #실패시 오류
    policy_link.raise_for_status()
    #string형태를 json으로 변환
    policy_string=json.loads(policy_link.text)
    #빈 데이터 dict 생성
    data={'area':[],
    'year':[],
    'title':[],
    'url':[]
    }
    #df를 위한 column
    columns = ['area','year','title','url']


    #데이터 dict에 적재
    for index in range(int(policy_string['item'][-1]['areaNo'])):
        for item in range(int(policy_string['item'][index]['itemCnt'])):
            data['area'].append(policy_string['item'][index]['areaNm'])
            data['year'].append(policy_string['item'][index]['items'][item]['year'])
            data['title'].append(policy_string['item'][index]['items'][item]['title'])
            data['url'].append(policy_string['item'][index]['items'][item]['url'])
    #data를 데이터 프레임으로 저장
    df=pd.DataFrame(data,columns=columns)
    df.to_csv(f'cp1_app/crawled_data_storage/policy_crawl_data_{query}.csv',encoding='utf-8-sig', index=False)
    return df

#외식업 관련 뉴스 크롤링(스크래핑) 함수(페이지수 입력)
def news_crawl(page=1):
    #네이버 기준 1년 '외식업' 기사링크
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%99%B8%EC%8B%9D%EC%97%85&sort=0&photo=0&field=0&pd=5&ds=2022.01.11&de=2023.01.11&cluster_rank=69&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:1y,a:all&start={page-1}1'

    url_req= requests.get(url)
    url_html = BeautifulSoup(url_req.text,'html.parser')

    news= url_html.select('div.group_news > ul.list_news > li div.news_area > a')

    data = {'title':[],
    'url':[],
    'content':[]}

    for i in news:
        data['title'].append(i.attrs['title'])
        data['url'].append(i.attrs['href'])
        contents=requests.get(i.attrs['href'])
        contents=BeautifulSoup(contents.text,'html.parser')
        data['content'].append(contents.find_all('p'))

    df = pd.DataFrame(data,columns=list(data.keys()))
    df.to_csv(f'cp1_app/crawled_data_storage/news_crawl_data_{num}.csv',encoding='utf-8-sig', index=False)
    return df

