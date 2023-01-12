import kosis_key 
import pandas as pd
import os
import pymysql

#불러올 데이터 
raw_database_path= '/Users/joshsong/Coding/Bootcamp/CP/CP1/raw_data'
normal_restaurant_path = raw_database_path+'/fulldata_07_24_04_P_일반음식점.csv'
rest_restaurant_path = raw_database_path+'/fulldata_07_24_05_P_휴게음식점.csv'

#데이터 불러와서 확인
normal_restaurant=pd.read_csv(normal_restaurant_path,low_memory=False, encoding='cp949')
rest_restaurant=pd.read_csv(rest_restaurant_path,low_memory=False, encoding='cp949')

#합치기 전 columns이 같은지 확인
# print((normal_restaurant.columns == rest_restaurant.columns))

#데이터 합치기
restaurant = pd.concat([normal_restaurant,rest_restaurant])

#columns 확인
# print(restaurant.columns)

#이상한 column 확인 후 제거
# print(restaurant['Unnamed: 47'])
# print(restaurant.info())
# print(restaurant.isnull().sum())

restaurant=restaurant.drop(columns=['Unnamed: 47', '홈페이지', '인허가취소일자',
'휴업시작일자','휴업종료일자','재개업일자','건물소유구분명','번호','개방서비스아이디'])

print(restaurant.isnull().sum())