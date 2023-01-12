import db_maker
import pymysql

#불러올 데이터 
raw_database_path= '/Users/joshsong/Coding/Bootcamp/CP/CP1/raw_data'
normal_restaurant_path = raw_database_path+'/fulldata_07_24_04_P_일반음식점.csv'
rest_restaurant_path = raw_database_path+'/fulldata_07_24_05_P_휴게음식점.csv'

db_maker.make_db('cp1')

# db,cur = db_maker.make_cursor('cp1_db','new')

def mounting_csv(db,csv_path, name):
    mounting_csv= f'''
    LOAD DATA LOCAL INFILE {csv_path}
    INTO TABLE {db}.{name} FIELDS TERMINATED BY ","
    IGNORE 1 ROWS;
    '''

    cur.execute(mounting_csv)

mounting_csv(db,normal_restaurant_path,'restaurant')
# mounting_csv(db,rest_restaurant_path,'restaurant')
db.commit()
db.close()