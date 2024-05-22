import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from selenium.common.exceptions import SessionNotCreatedException
import send2 as send2
import send1 as send1
import sys
import os


#declare app
window = Tk()

# Reference: https://stackoverflow.com/questions/71006377/tkinter-icon-is-not-working-after-converting-to-exe
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


frame = tk.Frame(window)
iconPath = resource_path('icon.ico')
window.iconbitmap(iconPath)
window.title("Blast WhatsApp Group")

# declare_layout
pic_lbl_path = tk.Label(frame, text='Image Path:', padx=25, pady=25, font=('verdana',16))
pic_lbl_show = tk.Label(frame)
pic_path = tk.Entry(frame, font=('verdana',16))
pic_btn_browse = tk.Button(frame, text='Select Image',bg='grey',font=('verdana',16))

csv_lbl_path = tk.Label(frame, text='File Path:', padx=25, pady=25, font=('verdana',16))
csv_lbl_show = tk.Label(frame)
csv_path = tk.Entry(frame, font=('verdana',16))
csv_btn_browse = tk.Button(frame, text='Select CSV',bg='grey',font=('verdana',16))

btn_send1 = tk.Button(frame, text='Send Without Poster',bg='grey',font=('verdana',16))
btn_send2 = tk.Button(frame, text='Send With Poster',bg='grey',font=('verdana',16))


### Logic

def SelectPic():
    global img
    global img_path
    get_pic = filedialog.askopenfilename(initialdir="/images", title="Select Image",filetypes=(("png images","*.png"),("jpg images","*.jpg")))
    img = Image.open(get_pic)
    img = img.resize((200,200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    pic_lbl_show['image'] = img
    pic_path.insert(0, get_pic)
    img_path = get_pic
    

def SelectCSV():
    global csv_path
    get_csv = filedialog.askopenfilename(title="Select File CSV",filetypes=(("CSV Files","*.csv"),))
    csv_path.insert(0,get_csv)
    csv_path=get_csv

def ButtonSend1():
    try:
        send1.Send(csv_path, window)
        window.update()
    except SessionNotCreatedException:
        messagebox.showinfo(title="ERROR!", message="Tutup Chrome Sebelumnya!")

def ButtonSend2():
    try:
        send2.Send(csv_path,img_path, window)
        window.update()
    except SessionNotCreatedException:
        messagebox.showinfo(title="ERROR!", message="Tutup Chrome Sebelumnya!")



### show layout

pic_btn_browse['command'] = SelectPic
csv_btn_browse['command'] = SelectCSV
btn_send1['command'] = ButtonSend1
btn_send2['command'] = ButtonSend2


frame.pack()

csv_lbl_path.grid(row=1, column=0)
csv_path.grid(row=1, column=1, padx=(0,20))
csv_btn_browse.grid(row=2, column=0, columnspan="2")
csv_lbl_show.grid(row=3, column=0, columnspan="2")

pic_lbl_path.grid(row=4, column=0)
pic_path.grid(row=4, column=1, padx=(0,20))
pic_btn_browse.grid(row=5, column=0, columnspan="2")
pic_lbl_show.grid(row=6, column=0, columnspan="2")


btn_send1.grid(row=7, column=0, columnspan="2", pady=(30,10))
btn_send2.grid(row=8, column=0, columnspan="2", pady=(0,20))

window.mainloop()