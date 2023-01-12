import sqlite3
import pandas as pd

conn = sqlite3.connect('cp1.db')
cur = conn.cursor()

sql_table='''CREATE TABLE IF NOT EXISTS restaurant (
    service_name VARCHAR(32),
    region_code VARCHAR(32),
    id_num VARCHAR(128) PRIMARY,
    permission_date TEXT,
    status VARCHAR(32),
    closed_date TEXT,
    shop_area FLOAT,
    address VARCHAR(255),
    road_address VARCHAR(255),
    name VARCHAR(255),
    recent_revised_date TEXT,
    data_update_date TEXT,
    classification VARCHAR(32),
    coord_x FLOAT,
    coord_y FLOAT,
    classification_sanitation VARCHAR(32),
    male_worker INT,
    female_worker INT,
    region_classification VARHCAR(64),
    rank_classification VARCHAR(32),
    water_source VARCHAR(255),
    multi_use_facility VARCHAR(255),
    total_area FLOAT,
    traditional_id VARCHAR(255),
    traditional_food VARCHAR(255)
);'''
cur.execute(sql_table)

conn.commit()

sql_insert="""INSERT INTO restaurant (
    service_name,region_code,id_num,permission_date,status,closed_date,shop_area,address,
    road_address,name,recent_revised_date,data_update_date,classification,coord_x,coord_y,
    classification_sanitation,male_worker,female_worker,region_classification,rank_classification,water_source,multi_use_facility,
    total_area,traditional_id,traditional_food) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
data = pd.read_csv('./processed_data/restaurant.csv')

for index, row in data.iterrows():
    cur.execute(sql_insert,(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24]))
conn.commit()
cur.close()