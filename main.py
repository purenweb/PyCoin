import os
import sys
import threading
import tkinter as tk
from datetime import datetime
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# import everything from tkinter module
from tkinter import *

# קריאה לפונקציה בקובץ אחר
from DataConn import *
import ReadJson
from ReadJson import *

# create a tkinter window
root = Tk()
# root.state('zoomed')
root.state('normal')


# נתיב נוכחי
def rcpath(rel_path):
    return os.path.join(os.getcwd(), rel_path)


# root.iconbitmap('@' + rcpath('icons/pypad.ico'))

root.iconbitmap('pic/money.ico')
# Open window having dimension 100x100
root.geometry('1000x500')
Canvas = Canvas(root)
Canvas.pack()

global a1
a1 = "ooo"


def prvGetData():
    try:
        GetNewData = ReadJson()
        Dogecoin, Bitcoin, XRP, BitTorrent, sTime, sDate = GetNewData.split(",")
        PubExecute(
            "INSERT INTO [dbo].[T_CoinNew] ([CoinDesc],[CoinNo],[CoinPrice]) VALUES ('Dogecoin',1," + Dogecoin + ")")
        PubExecute(
            "INSERT INTO [dbo].[T_CoinNew] ([CoinDesc],[CoinNo],[CoinPrice]) VALUES ('Bitcoin',1," + Bitcoin + ")")
        PubExecute("INSERT INTO [dbo].[T_CoinNew] ([CoinDesc],[CoinNo],[CoinPrice]) VALUES ('XRP',1," + XRP + ")")
        PubExecute(
            "INSERT INTO [dbo].[T_CoinNew] ([CoinDesc],[CoinNo],[CoinPrice]) VALUES ('BitTorrent',1," + BitTorrent + ")")
        lab1.config(text=Dogecoin)
        lab2.config(text=Bitcoin)
        lab3.config(text=XRP)
        lab4.config(text=BitTorrent)
        lab5.config(text="Last CAll")
        lab55.config(text=sTime)

        lab11.config(text=(str(float(Dogecoin) * float(txt1.get("1.0", END)))))
        lab22.config(text=(str(float(Bitcoin) * float(txt2.get("1.0", END)))))
        lab33.config(text=(str(float(XRP) * float(txt3.get("1.0", "end-1c")))))
        lab44.config(text=(str(float(BitTorrent) * float(txt4.get("1.0", "end-1c")))))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def paintGraph():
    Canvas.delete("all")
    iYTop = 2600
    iAmpli = 0.5
    iXStart = 10

    data = PubExecuteScalar(
        "SELECT   TOP (100) PERCENT  CoinPrice * 7524.1702 AS Expr1,RowNo FROM (SELECT TOP (5000) RowNo, CoinDesc, CoinNo, CoinPrice, InDate FROM  dbo.T_CoinNew ORDER BY RowNo DESC) AS derivedtbl_1   WHERE (CoinDesc = N'Dogecoin') ORDER BY RowNo ")

    i = iXStart
    ixLast = 0
    iyLast = 0
    iXSpace = 1.2
    for row in data:
        print("Id = ", row[0], )
        i = i + 1
        y = (iYTop - (row[0] / iAmpli)) * 1.2
        if ixLast == 0: ixLast = i * iXSpace
        if iyLast == 0: iyLast = y

        Canvas.create_line(ixLast, iyLast, i * iXSpace + 1, y + 1, fill="#f00042")
        ixLast = i * iXSpace
        iyLast = y
    data = PubExecuteScalar(
        "SELECT   TOP (100) PERCENT  CoinPrice * 1750 AS Expr1,RowNo FROM (SELECT TOP (5000) RowNo, CoinDesc, CoinNo, CoinPrice, InDate FROM  dbo.T_CoinNew ORDER BY RowNo DESC) AS derivedtbl_1   WHERE (CoinDesc = N'XRP') ORDER BY RowNo ")

    i = iXStart
    ixLast = 0
    iyLast = 0
    iXSpace = 1.2
    for row in data:
        print("Id = ", row[0], )
        i = i + 1
        y = (iYTop - (row[0] / iAmpli)) * 1.2
        if ixLast == 0: ixLast = i * iXSpace
        if iyLast == 0: iyLast = y

        Canvas.create_line(ixLast, iyLast, i * iXSpace + 1, y + 1, fill="#660042")
        ixLast = i * iXSpace
        iyLast = y
    data = PubExecuteScalar(
        "SELECT   TOP (100) PERCENT  CoinPrice * 0.029 AS Expr1,RowNo FROM (SELECT TOP (5000) RowNo, CoinDesc, CoinNo, CoinPrice, InDate FROM  dbo.T_CoinNew ORDER BY RowNo DESC) AS derivedtbl_1   WHERE (CoinDesc = N'Bitcoin') ORDER BY RowNo ")

    i = iXStart
    ixLast = 0
    iyLast = 0
    iXSpace = 1.2
    for row in data:
        print("Id = ", row[0], )
        i = i + 1
        y = (iYTop - (row[0] / iAmpli)) * 1.2
        if ixLast == 0: ixLast = i * iXSpace
        if iyLast == 0: iyLast = y

        Canvas.create_line(ixLast, iyLast, i * iXSpace + 1, y + 1, fill="#ABAB57")
        ixLast = i * iXSpace
        iyLast = y
    # data = PubExecuteScalar(
    #     "SELECT   TOP (100) PERCENT  CoinPrice * 460000 AS Expr1,RowNo FROM (SELECT TOP (6690) RowNo, CoinDesc, CoinNo, CoinPrice, InDate FROM  dbo.T_CoinNew ORDER BY RowNo DESC) AS derivedtbl_1   WHERE (CoinDesc = N'BitTorrent') AND (CoinPrice < 1) AND (CoinPrice > 0.001) ORDER BY RowNo ")
    #
    # i = iXStart
    # ixLast = 0
    # iyLast = 0
    # iXSpace = 1.2
    # for row in data:
    #     print("Id = ", row[0], )
    #     i = i + 1
    #     y = (iYTop - (row[0] / iAmpli*0.9)) * 1.2
    #     if ixLast == 0: ixLast = i * iXSpace
    #     if iyLast == 0: iyLast = y
    #
    #     Canvas.create_line(ixLast, iyLast, i * iXSpace + 1, y + 1, fill="#325DA8")
    #     ixLast = i * iXSpace
    #     iyLast = y


def paint(event):
    Canvas.create_oval(120, 120, 180, 180)
    python_green = "#fff042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_green)
    w.create_oval(20, 20, 80, 80, fill=python_green)


def Close():
    root.destroy()
    sys.exit()


w = Canvas
w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)

# Create a Button
btn1 = Button(root, text='קרא נתונים !', bd='2', command=prvGetData, width=10, height=1)
btn1.place(x=100, y=400)
btn2 = Button(root, text='סגור', bd='2', command=Close, width=10, height=1)
btn2.place(x=200, y=400)
btn3 = Button(root, text='!', bd='2', command=paintGraph, width=10, height=1)
btn3.place(x=300, y=400)


def prvCB1():
    if var1.get() == 1:
        prvGetData


# checkBox
var1 = IntVar()
cb1 = Checkbutton(root, text="male", variable=var1, command=prvCB1)
cb1.place(x=200, y=200)

# Set the position of button on the top of window.
xP = 125
yP = 20
xS = 0
yS = 40

lab1 = Label(root, text=a1)
lab1.pack()
lab1.place(x=xP - 30, y=yP)
lab2 = Label(root, text=a1)
lab2.pack()
lab2.place(x=xP - 30, y=yP + yS * 1)
lab3 = Label(root, text=a1)
lab3.pack()
lab3.place(x=xP - 30, y=yP + yS * 2)
lab4 = Label(root, text=a1)
lab4.pack()
lab4.place(x=xP - 30, y=yP + yS * 3)
lab5 = Label(root, text=a1)
lab5.pack()
lab5.place(x=xP - 30, y=yP + yS * 4)

lab11 = Label(root, text=a1)
lab11.pack()
lab11.place(x=xP + 250, y=yP)
lab22 = Label(root, text=a1)
lab22.pack()
lab22.place(x=xP + 250, y=yP + yS * 1)
lab33 = Label(root, text=a1)
lab33.pack()
lab33.place(x=xP + 250, y=yP + yS * 2)
lab44 = Label(root, text=a1)
lab44.pack()
lab44.place(x=xP + 250, y=yP + yS * 3)
lab55 = Label(root, text=a1)
lab55.pack()
lab55.place(x=xP + 250, y=yP + yS * 4)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
root.title(current_time)

txt1 = Text(root, height=1, width=15)
txt1.pack()
txt1.place(x=xP + 100, y=yP)
txt2 = Text(root, height=1, width=15)
txt2.pack()
txt2.place(x=xP + 100, y=yP + yS * 1)
txt3 = Text(root, height=1, width=15)
txt3.pack()
txt3.place(x=xP + 100, y=yP + yS * 2)
txt4 = Text(root, height=1, width=15)
txt4.pack()
txt4.place(x=xP + 100, y=yP + yS * 3)
txt5 = Text(root, height=1, width=15)
txt5.pack()
txt5.place(x=xP + 100, y=yP + yS * 4)
txt1.insert(tk.END, "7524.1702")
txt2.insert(tk.END, "0")
txt3.insert(tk.END, "0")
txt4.insert(tk.END, "0")
txt5.insert(tk.END, "0")


def f(f_stop):
    prvGetData()
    paintGraph()
    if not f_stop.is_set():
        # call f() again in 60 seconds
        threading.Timer(600, f, [f_stop]).start()


f_stop = threading.Event()
# start calling f now and every 60 sec thereafter
f(f_stop)

# stop the thread when needed
# f_stop.set()

root.mainloop()
