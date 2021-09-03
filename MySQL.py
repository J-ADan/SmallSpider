import sqlite3
from Mydata import *

db_name = 'My.db'


def Create_table():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        create table movie(
            id integer primary key autoincrement,
            name text primary key,
            star text,
            time text,
            country text,
            score float 
        )
    ''')
    conn.commit()
    conn.close()


def Savem(index, id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        insert into movie
        (name,star,time,country,score)
        values 
        (?,?,?,?,?)
    ''', (get_name(index, id), get_star(index, id), get_time(index, id), get_country(index, id), get_score(index, id))
                   )
    conn.commit()
    conn.close()


def Inquire_idm(id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
    select * from movie WHERE id = ?
    ''', (id,)
                   )
    return cursor.fetchall()


def Inquire_namem(name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        select * from movie WHERE name = ?
        ''', (name,)
                   )
    return cursor.fetchall()


def Delete_allm():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        delete from movie;
    ''')
    cursor.execute('''
    update sqlite_sequence SET seq = 0 where name ='movie'
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    for i in range(0, 2):
        for j in range(0, 10):
            Savem(i, j)
    # Delete_allm()

