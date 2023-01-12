import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import sqlite3




API_KEY = 'fk5c936Rh31iz1G42vUaX8SWFdSEt61U2A9yH1hV'
DB_NAME = 'cp1.db'
DB_PATH = os.path.join(os.getcwd(),DB_NAME)

def get_data(month,API_KEY=API_KEY):
    api_url=f'https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2022&month={month}&apiKey={API_KEY}&returnType=json'
    response=requests.get(api_url)
    text_data=response.text
    data_split=text_data.split('}{')
    data_split[0]=data_split[0]+'}'
    data_split[1]='{'+data_split[1]
    data=data_split
    
    main_data=json.loads(data[1])
    main_data=main_data['data']
    
    
    return main_data


def connect_to_db(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    return conn, cur


conn, cur = connect_to_db(DB_PATH)
cur.execute("""CREATE TABLE IF NOT EXISTS main_data(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
year INTEGER,
month INTEGER,
metro VARCHAR,
city VARCHAR,
biz VARCHAR,
custCnt INTEGER,
powerUsage INTEGER,
bill INTEGER,
unitCost FLOAT);""")

for m in range(1,12):
            
            if (m != 10)&(m != 11):
                m='0'+str(m)
            else:
                m=str(m)
            main_data=get_data(month=m)
            for i in main_data:
                cur.execute("INSERT INTO main_data (year,month,metro,city,biz,custCnt,powerUsage,bill,unitCost) VALUES(?,?,?,?,?,?,?,?,?);",list(i.values()))



conn.commit()
conn.close()
print('Finished')