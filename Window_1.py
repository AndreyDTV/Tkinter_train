import tkinter as tk


def add_text(person):
    value = display.get()
    if len(value) != 0:
        display.delete(0, 'end')
    if person == 'Сэр':
        display.insert(0, 'Сэр-самый лучший кот в мире!')
    elif person == 'Казаки':
        display.insert(0, 'Любимая обувь Машульки!')
    elif person == 'Машулька':
        display.insert(0, next(iter(['Крашиха Андрея!','Настоящая леди','Неописуемая красотка'])))
    elif person == 'Андрей':
        display.insert(0, 'Друг Сэра!')


def make_button(person):
    return tk.Button(win, text=person, font=('Comics', 12), bd=5, command=lambda: add_text(person))


win = tk.Tk()
win.geometry('300x300')
win.resizable(False, False)
win.configure(bg='#FFDEAD')

display = tk.Entry(win, justify=tk.CENTER, font=('Comics', 15, 'bold'), width=20)
display.grid(row=0, column=0, columnspan=2, rowspan=2, padx=5, stic='wens')

make_button('Сэр').grid(row=2, column=0, stic='wens', padx=5, pady=5)
make_button('Андрей').grid(row=3, column=0, stic='wens', padx=5, pady=5)
make_button('Машулька').grid(row=2, column=1, stic='wens', padx=5, pady=5)
make_button('Казаки').grid(row=3, column=1, stic='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=150)
win.grid_columnconfigure(1, minsize=150)

win.grid_rowconfigure(0, minsize=150)
win.grid_rowconfigure(2, minsize=75)
win.grid_rowconfigure(3, minsize=75)

win.mainloop()
