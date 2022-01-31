import tkinter as tk

def update_scrollregion(event):
    photoCanvas.configure(scrollregion=photoCanvas.bbox("all"))

root = tk.Tk()


photoFrame = tk.Frame(root, width=250, height=190, bg="#EBEBEB")
photoFrame.grid()
photoFrame.rowconfigure(0, weight=1)
photoFrame.columnconfigure(0, weight=1)

photoCanvas = tk.Canvas(photoFrame, bg="#EBEBEB")
photoCanvas.grid(row=0, column=0, sticky="nsew")

canvasFrame = tk.Frame(photoCanvas, bg="#EBEBEB")
photoCanvas.create_window(0, 0, window=canvasFrame, anchor='nw')

for i in range(10):
   element = tk.Button(canvasFrame, text='Button %i' % i, borderwidth=0, bg="#EBEBEB")
   element.grid(padx=5, pady=5, sticky="nsew")

photoScroll = tk.Scrollbar(photoFrame, orient=tk.VERTICAL)
photoScroll.config(command=photoCanvas.yview)
photoCanvas.config(yscrollcommand=photoScroll.set)
photoScroll.grid(row=0, column=1, sticky="ns")

canvasFrame.bind("<Configure>", update_scrollregion)

root.mainloop()