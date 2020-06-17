from tkinter import *

from pypresence import Presence

import time

client_id = "718896866443526175"

RPC = Presence(client_id)

RPC.connect()

def update():

    milliseconds = int(round(time.time() * 1000))

    rpc_state = state.get()
    rpc_img = img.get()
    rpc_text = tooltip.get()


    RPC.update(
        state = rpc_state,
        start = milliseconds,
        large_image = rpc_img,
        large_text = rpc_text
    )

def clear(): 
    state.delete(0, END)
    img.delete(0, END)
    tooltip.delete(0, END)

    RPC.clear()

def quit():
    RPC.close()
    master.quit()

master = Tk()
master.title("Slowly™")
master.geometry("225x125")
master.resizable(0, 0)

Label(master, text="State").grid(row=0, column=0)
Label(master, text="Image").grid(row=1, column=0)
Label(master, text="Tooltip").grid(row=2, column=0)

state = Entry(master, width=26)
state.grid(row=0, column=1, columnspan=6, pady=4)
img = Entry(master, width=26)
img.grid(row=1, column=1, columnspan=6, pady=4)
tooltip = Entry(master, width=26)
tooltip.grid(row=2, column=1, columnspan=6, pady=4)

Button(master, text="Update", command=update).grid(row=3, column=1, sticky=W, pady=4)
Button(master, text="Clear", command=clear).grid(row=3, column=3, sticky=W, pady=4)
Button(master, text="Quit", command=quit).grid(row=3, column=5, sticky=W, pady=4)

master.mainloop( )