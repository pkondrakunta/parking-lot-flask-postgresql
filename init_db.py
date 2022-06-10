import os
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
)

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS parking_spaces;')
cur.execute('CREATE TABLE parking_spaces (id serial PRIMARY KEY,' 'number varchar(3) NOT NULL,' 'status varchar(10) NOT NULL);'
)

cur.execute('INSERT INTO parking_spaces (number, status)' 'VALUES (%s, %s)', ('001', 'Vacant'))
cur.execute('INSERT INTO parking_spaces (number, status)' 'VALUES (%s, %s)', ('002', 'Vacant'))
cur.execute('INSERT INTO parking_spaces (number, status)' 'VALUES (%s, %s)', ('003', 'Vacant'))
cur.execute('INSERT INTO parking_spaces (number, status)' 'VALUES (%s, %s)', ('004', 'Vacant'))


conn.commit()
cur.close()
conn.close()