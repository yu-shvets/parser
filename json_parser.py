import json
import pymysql


# Deserializing json file

with open('eFw3Cefj.json') as data_file:
    data = json.load(data_file)

data = data['data']


# Setting up MySQL connection

conn = pymysql.connect(
     host='localhost',
     user='info_db_user',
     password='parser',
     db='info_db',
     charset='utf8',
     cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()


# Creating tables

cursor.execute('CREATE TABLE groups (регион VARCHAR(40) PRIMARY KEY) ENGINE=InnoDB;')
cursor.execute('CREATE TABLE info (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, регион VARCHAR(40), страна VARCHAR(40), '
               'параметры DECIMAL, FOREIGN KEY(регион) REFERENCES groups(регион)) ENGINE=InnoDB;')


# Injecting data

for i in data:

    region = i['Регион']
    country = i['Страна']
    rate = i['Значение']

    cursor.execute('INSERT IGNORE INTO groups(регион) values (%s)', region)
    cursor.execute('INSERT INTO info(регион, страна, параметры) values (%s, %s, %s)', (region, country, rate))

conn.commit()
conn.close()




