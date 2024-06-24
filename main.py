import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from selenium.common.exceptions import SessionNotCreatedException
import picture1 as picture1
import wording1 as wording1
import picture2 as picture2
import wording2 as wording2
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

btn_wording1 = tk.Button(frame, text='text only 1',bg='grey',font=('verdana',16))
btn_wording2 = tk.Button(frame, text='text only 2',bg='grey',font=('verdana',16))
btn_picture1 = tk.Button(frame, text='Poster + 1 text',bg='grey',font=('verdana',16))
btn_picture2 = tk.Button(frame, text='Poster + 2 text',bg='grey',font=('verdana',16))


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

def Buttonwording1():
    try:
        wording1.Send(csv_path, window)
        window.update()
    except SessionNotCreatedException:
        messagebox.showinfo(title="ERROR!", message="Tutup Chrome Sebelumnya!")

def Buttonwording2():
    try:
        wording2.Send(csv_path, window)
        window.update()
    except SessionNotCreatedException:
        messagebox.showinfo(title="ERROR!", message="Tutup Chrome Sebelumnya!")

def Buttonpicture1():
    try:
        picture1.Send(csv_path,img_path, window)
        window.update()
    except SessionNotCreatedException:
        messagebox.showinfo(title="ERROR!", message="Tutup Chrome Sebelumnya!")

def Buttonpicture2():
    try:
        picture2.Send(csv_path,img_path, window)
        window.update()
    except SessionNotCreatedException:
        messagebox.showinfo(title="ERROR!", message="Tutup Chrome Sebelumnya!")



### show layout

pic_btn_browse['command'] = SelectPic
csv_btn_browse['command'] = SelectCSV
btn_wording1['command'] = Buttonwording1
btn_picture1['command'] = Buttonpicture1
btn_wording2['command'] = Buttonwording2
btn_picture2['command'] = Buttonpicture2


frame.pack()

csv_lbl_path.grid(row=1, column=0)
csv_path.grid(row=1, column=1, padx=(0,20))
csv_btn_browse.grid(row=2, column=0, columnspan="2")
csv_lbl_show.grid(row=3, column=0, columnspan="2")

pic_lbl_path.grid(row=4, column=0)
pic_path.grid(row=4, column=1, padx=(0,20))
pic_btn_browse.grid(row=5, column=0, columnspan="2")
pic_lbl_show.grid(row=6, column=0, columnspan="2")


btn_wording1.grid(row=7, column=0, columnspan="2", pady=(30,10))
btn_wording2.grid(row=8, column=0, columnspan="2", pady=(10,10))
btn_picture1.grid(row=9, column=0, columnspan="2", pady=(30,10))
btn_picture2.grid(row=10, column=0, columnspan="2", pady=(10,10))

window.mainloop()