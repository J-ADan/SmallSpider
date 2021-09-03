import tkinter as tk
from tkinter import ttk
from tkinter import *
from ZhSQL import *
from MySQL import *


def finction():
    def Updatef():
        Delete_allz()
        for i in range(0, 2):
            for j in range(0, 20):
                Savez(i, j)

    def Inquiref():
        id = entry1.get()
        inre = Inquire_idz(id)
        t.insert('insert', inre)

    def Inquiref1():
        name = entry2.get()
        inre = Inquire_namez(name)
        t.insert('insert', inre)

    def allz():
        Inquiref()
        Inquiref1()

    windows1 = tk.Tk()
    windows1.title('Fiction')
    windows1.geometry('800x500')
    lable1 = Label(windows1, text='Id', font=('Arial', 12))
    lable1.place(x=10, y=10)
    entry1 = tk.Entry(windows1, show=None, font=('Arial', 12))
    entry1.place(x=80, y=10)

    lable2 = Label(windows1, text='Name', font=('Arial', 12))
    lable2.place(x=400, y=10)
    entry2 = tk.Entry(windows1, show=None, font=('Arial', 12))
    entry2.place(x=480, y=10)

    butc = Button(windows1, text='查询详细数据', height=2, width=10, command=allz)
    butc.place(x=300, y=40)
    '''listView'''
    columns = ("id", "name", "reader", "last", "time", "type", "status")
    headers = ("排名", "书名", "作者", "最新章节", "更新时间", "类型", "状态")
    widthes = (50, 100, 100, 150, 120, 50, 50)

    # 列表视图显示
    tv = ttk.Treeview(windows1, show="headings", columns=columns)
    for (column, header, width) in zip(columns, headers, widthes):
        tv.column(column, width=width, anchor="w")
        tv.heading(column, text=header, anchor="w")

    def inser_data():
        datalist = []
        conn = sqlite3.connect('Zh.db')
        cur = conn.cursor()
        for i in range(1, 11):
            cur.execute('''
                                SELECT * FROM fiction WHERE id=?
                    ''', (i,)
                        )
            data = cur.fetchall()
            datalist.append(data[0])
        for j in range(0, 10):
            data1 = list(datalist[j])
            del data1[5]
            del data1[3]
            datalist[j] = data1
        # 数据显示
        contacts = [
            datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6], datalist[7],
            datalist[8], datalist[9]
        ]
        for i, person in enumerate(contacts):
            tv.insert('', i, values=person)

    inser_data()

    tv.place(x=80, y=100)

    t = tk.Text(windows1, height=8, width=55)
    t.place(x=80, y=350)

    but = Button(windows1, text='更新小说数据', height=5, width=20, command=Updatef)
    but.place(x=500, y=350)

    windows1.mainloop()


def movie():
    def Updatem():
        Delete_allm()
        for i in range(0, 2):
            for j in range(0, 10):
                Savem(i, j)

    def Inquirem():
        id = entry1.get()
        inre = Inquire_idm(id)
        t.insert('insert', inre)

    def Inquirem1():
        name = entry2.get()
        inre = Inquire_namem(name)
        t.insert('insert', inre)

    def allm():
        Inquirem()
        Inquirem1()

    windows2 = tk.Tk()
    windows2.title('Movie')
    windows2.geometry('800x500')

    lable1 = Label(windows2, text='Id', font=('Arial', 12))
    lable1.place(x=10, y=10)
    entry1 = tk.Entry(windows2, show=None, font=('Arial', 12))
    entry1.place(x=80, y=10)

    lable2 = Label(windows2, text='Name', font=('Arial', 12))
    lable2.place(x=400, y=10)
    entry2 = tk.Entry(windows2, show=None, font=('Arial', 12))
    entry2.place(x=480, y=10)
    butc = Button(windows2, text='查询详细数据', height=2, width=10, command=allm)
    butc.place(x=300, y=40)

    columns = ("id", "name", "star", "time", "country", "score")
    headers = ("排名", "电影名字", "明星主演", "上映时间", "国家", "猫眼评分")
    widthes = (40, 150, 170, 100, 80, 60)
    tv = ttk.Treeview(windows2, show="headings", columns=columns)

    for (column, header, width) in zip(columns, headers, widthes):
        tv.column(column, width=width, anchor="w")
        tv.heading(column, text=header, anchor="w")

    def inser_data():
        datalist = []
        conn = sqlite3.connect('My.db')
        cur = conn.cursor()
        for i in range(1, 11):
            cur.execute('''
                                SELECT * FROM movie WHERE id=?
                    ''', (i,)
                        )
            data = cur.fetchall()
            datalist.append(data[0])
        contacts = [
            datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6], datalist[7],
            datalist[8], datalist[9]
        ]
        for i, person in enumerate(contacts):
            tv.insert('', i, values=person)

    inser_data()

    tv.place(x=80, y=100)

    t = tk.Text(windows2, height=8, width=55)
    t.place(x=80, y=350)

    but = Button(windows2, text='更新电影数据', height=5, width=20, command=Updatem)
    but.place(x=500, y=350)

    windows2.mainloop()


if __name__ == '__main__':
    # finction()
    movie()

