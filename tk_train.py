import random
from tkmacosx import Button


# def set_label_1():
#     colors = ['red', 'yellow', 'blue']
#     lable_1 = tk.Label(win, width=20, height=20, text='Привет!', bg=random.choice(colors), font='Arial',
#                        relief=tk.GROOVE, bd=10)
#     lable_1.pack(anchor='center', pady=200)
#
#
# def change_win():
#     m = win.geometry()
#     if m == "600x500+5+30":
#         win.geometry('300x300')
#     else:
#         win.geometry('600x500')


import tkinter as tk
from tkmacosx import Button

win = tk.Tk()
print(win.geometry())
win.geometry(f"600x500")
win.title("Новое окно")
win.configure(bg='#ADD8E6')

# btn_1 = Button(win, text='Press start', font='Arial',
#                activebackground='red',
#                command=set_label_1,
#                bg='yellow')
# btn_2 = Button(win, text='Change size win',command=change_win)
# btn_2.pack()
# btn_1.pack()
# print(tk.Tk.__dict__)
# win.mainloop()
