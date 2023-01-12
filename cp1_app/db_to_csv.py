import sqlite3
import pandas as pd

con = sqlite3.connect('cp1.db')
cur = con.cursor()

query = cur.execute('SELECT * FROM main_data')
cols = [column[0] for column in query.description]

df = pd.DataFrame.from_records(data=query.fetchall(), columns = cols)
df.to_csv('processed_data/electricity_pay.csv', index=False)

query = cur.execute('SELECT * FROM restaurant')
cols = [column[0] for column in query.description]

df = pd.DataFrame.from_records(data=query.fetchall(), columns = cols)
df.to_csv('processed_data/restaurant_db.csv', encoding='utf8', index=False)

con.close()