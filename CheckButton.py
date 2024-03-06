import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def toggle_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


def show():
    print('Значение over_18_value:', over_18_value.get())
    print('Значение commercial_value:', commercial_value.get())


win = tk.Tk()
win.geometry('300x300')
win.title('Новая тренировка')

over_18_value = tk.StringVar()
over_18_value.set('NO')


over_18 = tk.Checkbutton(win, text='Вам исполнилось 18 лет?', variable=over_18_value,
                         offvalue='NO',
                         onvalue='YES')

commercial_value = tk.IntVar()

commercial = tk.Checkbutton(win, text='Хотите получать рекламу?', variable=commercial_value,
                         offvalue=0,
                         onvalue=1)
follow = tk.Checkbutton(win, text='Хотите подписаться на канал?', indicatoron=0)

over_18.pack()
commercial.pack()
follow.pack()

tk.Button(text='select all', command=select_all).pack()
tk.Button(text='deselect all', command=deselect_all).pack()
tk.Button(text='toggle all', command=toggle_all).pack()
tk.Button(text='show_over_18_value', command=show).pack()
win.mainloop()
