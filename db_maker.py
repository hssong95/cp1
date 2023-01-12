import pymysql
import mysql_key as sqkey

# DB 만들기

def make_db(db_name,port=3000):
    conn = pymysql.connect(host=sqkey.host, user=sqkey.user, password=sqkey.pw, charset='utf8')

    cursor = conn.cursor()

    make_db_order = f'CREATE DATABASE {db_name};'

    cursor.execute(make_db_order)

    conn.commit()

    conn.close()

make_db('cp1')

def make_cursor(db_name, is_new=None, ):
    if is_new != None:
        db = pymysql.connect(host=sqkey.host, port=3000, user=sqkey.user, passwd=sqkey.pw, db=db_name)
    else:
        make_db(db_name)
        db = pymysql.connect(host=sqkey.host, port=3000, user=sqkey.user, passwd=sqkey.pw, db=db_name)

    cur = db.cursor
    return db,cur


