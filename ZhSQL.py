from Zhdata import *
import sqlite3

db_name = 'ZH.db'


def Create_table():
    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()
    cursor.execute('''
        create table fiction(
            id integer primary key autoincrement,
            name text primary key,
            reader text,
            info text,
            last text,
            ticket text,
            time text,
            type text,
            status text
        )
    ''')
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()


def Savez(index, id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        insert into fiction
        (name,reader,info,last,ticket,time,type,status)
        values 
        (?,?,?,?,?,?,?,?)
    ''', (get_name(index, id), get_reader(index, id), get_info(index, id), get_last(index, id),
          get_ticket(index, id), get_time(index, id), get_type(index, id), get_status(index, id))
                   )

    conn.commit()
    conn.close()


def Inquire_idz(id):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
    select * from fiction WHERE id = ?
    ''', (id,)
                   )
    return cursor.fetchall()


def Inquire_namez(name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        select * from fiction WHERE name = ?
        ''', (name,)
                   )
    return cursor.fetchall()


def Delete_allz():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''
        delete from fiction;
    ''')
    cursor.execute('''
    update sqlite_sequence SET seq = 0 where name ='fiction'
    ''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # for i in range(0, 2):
    #     for j in range(0, 20):
    #         Savez(i, j)
    # Delete_allz()
    Create_table()

