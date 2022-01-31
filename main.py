import os
from datetime import datetime, timedelta
from tkinter.ttk import Treeview
##XXXXXXXXXXXXXXXXXXXXXX
import self as self
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import tkinter as tk

# import everything from tkinter module
from tkinter import *

#קריאה לפונקציה בקובץ אחר
from DataConn import *

# def PubExecQuery(sSql):
#     IsEXE = (sSql[0:6])
#     con()
#     cursor.execute(sSql)
#     if IsEXE != 'SELECT': conn.commit()


# create a tkinter window
root = Tk()
#root.state('zoomed')
root.state('normal')

#נתיב נוכחי
def rcpath(rel_path):
    return os.path.join(os.getcwd(), rel_path)

#root.iconbitmap('@' + rcpath('icons/pypad.ico'))


root.iconbitmap('pic/money.ico')
# Open window having dimension 100x100
root.geometry('1000x500')
Canvas = Canvas(root)
Canvas.pack()

global a1
a1 = "ooo"


def prvGetData():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {'start': '1', 'limit': '100', 'convert': 'USD'}
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': '43f1bd77-3f44-46a4-9243-713738fabb72', }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        # print(data)
        # with open('c:\\temp\\o1.txt', 'w') as f:
        #  json.dump(data, f)

        y = json.dumps(data, indent=4, sort_keys=True)
        with open('c:\\temp\\o2.txt', 'w') as f1:
            json.dump(y, f1)

        def prvRes(Coin, y):
            iCoinPos = y.find(Coin)
            sCoinFull = (y[iCoinPos:4000 + iCoinPos])
            iCoinPricePos = sCoinFull.find("price")
            sCoinPriceFull = (sCoinFull[iCoinPricePos + 8:iCoinPricePos + 30])
            iPriceSplit = sCoinPriceFull.find(",")
            res = (sCoinPriceFull[0:iPriceSplit])
            PubExecute("INSERT INTO [dbo].[T_CoinNew] ([CoinDesc],[CoinNo],[CoinPrice]) VALUES ('" + Coin + "',1," + res + ")")
            return (sCoinPriceFull[0:iPriceSplit])

        import datetime as dt
        mytime = dt.datetime.strptime(y[212:220], '%H:%M:%S').time()

        mydatetime = dt.datetime.combine(dt.date.today(), mytime)+ timedelta(hours=2)
        today = mydatetime.strftime("%d/%m/%Y %H:%M:%S")

        from datetime import date

        a1 = prvRes("Dogecoin", y)
        a2 = prvRes("Bitcoin", y)
        a3 = prvRes("XRP", y)
        a4 = prvRes("BitTorrent", y)

        lab1.config(text=a1)
        lab2.config(text=a2)
        lab3.config(text=a3)
        lab4.config(text=a4)
        lab5.config(text="Last CAll")
        lab55.config(text=today)

        lab11.config(text=(str(float(a1) * float(txt1.get("1.0", "end-1c")))))
        lab22.config(text=(str(float(a2) * float(txt2.get("1.0", "end-1c")))))
        lab33.config(text=(str(float(a3) * float(txt3.get("1.0", "end-1c")))))
        lab44.config(text=(str(float(a4) * float(txt4.get("1.0", "end-1c")))))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def btn1_OnClick():
    # iUse=0
    #
    # from datetime import datetime
    # now = datetime.now()
    # RunMin = now.strftime("%M")[-1:]
    # if RunMin==9 and iUse==0:
    #     iUse=1
    prvGetData()


def btn2_OnClick():
    Canvas.delete("all")
    x = txt1.get("1.0", "end-1c")
    x1 = 1 * float(x)
    #lab3.config(text=(str(x1)))
    Canvas.create_oval(-10, 170, 11, 171)
    Canvas.create_oval(-10, 190, 11, 191)
    Canvas.create_oval(1, 265, 11, 266, fill="#fff042")
    #   time.sleep(600)
    iYTop = 2600
    iAmpli = 0.5
    iXStart = 10
    #PubExecuteScalar("SELECT  CoinPrice * 7524.1702 AS Expr1  FROM dbo.T_CoinNew WHERE (CoinDesc = N'Dogecoin') ")
    data =PubExecuteScalar("SELECT   TOP (100) PERCENT  CoinPrice * 7524.1702 AS Expr1,RowNo FROM (SELECT TOP (5000) RowNo, CoinDesc, CoinNo, CoinPrice, InDate FROM  dbo.T_CoinNew ORDER BY RowNo DESC) AS derivedtbl_1   WHERE (CoinDesc = N'Dogecoin') ORDER BY RowNo ")

#############################

    i = (iXStart)
    ixLast = 0
    iyLast = 0
    iXSpace=1.2
    for row in data:
        print("Id = ", row[0], )
        i = i + 1
        y = ((iYTop) - (row[0] / (iAmpli))) * 1.2
        if ixLast == 0: ixLast = i *iXSpace
        if iyLast == 0: iyLast = y

        Canvas.create_line(ixLast, iyLast, i * iXSpace + 1, y + 1, fill="#f00042")
        ixLast = i * iXSpace
        iyLast = y



def paint(event):
    Canvas.create_oval(120, 120, 180, 180)
    python_green = "#fff042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill=python_green)
    w.create_oval(20, 20, 80, 80, fill=python_green)


w = Canvas
w.pack(expand=YES, fill=BOTH)
w.bind("<B1-Motion>", paint)

# Create a Button
btn1 = Button(root, text='קרא נתונים !', bd='2', command=btn1_OnClick, width=10, height=1)
btn1.place(x=100, y=400)
btn2 = Button(root, text='סגור', bd='2', command=root.destroy, width=10, height=1)
btn2.place(x=200, y=400)
btn3 = Button(root, text='!', bd='2', command=btn2_OnClick, width=10, height=1)
btn3.place(x=300, y=400)


def prvCB1():
    if var1.get() == 1:
        btn1_OnClick


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
import threading

def f(f_stop):
    prvGetData()
    btn2_OnClick()
    if not f_stop.is_set():
        # call f() again in 60 seconds
        threading.Timer(600, f, [f_stop]).start()

f_stop = threading.Event()
# start calling f now and every 60 sec thereafter
f(f_stop)

# stop the thread when needed
#f_stop.set()

root.mainloop()
