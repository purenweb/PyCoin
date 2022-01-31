from tkinter import *
from DataConn import *

class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 14, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


# take the data
data =PubExecuteScalar("SELECT   top 100  CoinPrice * 7524.1702 AS Expr1,RowNo, CoinPrice  from T_CoinNew  WHERE (CoinDesc = N'Dogecoin') ORDER BY RowNo Desc ")
lst=[]

for row in data:
    Prelst = []
    Prelst.append(row[0])
    Prelst.append(row[1])
    Prelst.append(row[2])
    #FullLst =str(row[0])+","+str(row[1])+","+ str(row[2])
    lst.append(Prelst)


# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()