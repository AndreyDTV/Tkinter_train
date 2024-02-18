import tkinter as tk
from PIL import ImageTk


def add_digit(digit):
    value = display.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    display.delete(0, 'end')
    display.insert(0, value + digit)


def add_operation(operation):
    value = display.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = display.get()
    display.delete(0, 'end')
    display.insert(0, value + operation)


def calculate():
    value = display.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    display.delete(0, 'end')
    display.insert(0, eval(value))


def clear():
    value = display.get()
    if value != '':
        display.delete(0, 'end')
        display.insert(0, '0')


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 20), fg='red', command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 20), fg='red', command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 20), fg='red', command=clear)


win = tk.Tk()
win.title('Калькулятор')
win.geometry(f'250x280+100+200')
win['bg'] = '#ADD8E6'

display = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
display.insert(0, '0')
display.grid(row=0, column=0, columnspan=4, stic='wens', padx=5)

make_digit_button('1').grid(row=1, column=0, stic="wens", padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stic="wens", padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stic="wens", padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stic="wens", padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stic="wens", padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stic="wens", padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stic="wens", padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stic="wens", padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stic="wens", padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stic="wens", padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stic="wens", padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stic="wens", padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stic="wens", padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stic="wens", padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stic="wens", padx=5, pady=5)
make_clear_button('c').grid(row=4, column=1, stic="wens", padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(0, minsize=40)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
