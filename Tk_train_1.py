import tkinter as tk
from tkinter import messagebox


def add_digit(digit):  # Функция добавляет цифры в поле ввода
    value = display.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    display['state'] = tk.NORMAL
    display.delete(0, 'end')
    display.insert(0, value + digit)
    display['state'] = tk.DISABLED


def add_operation(operation):  # Функция добавляет знак математической операции в поле ввода
    value = display.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = display.get()
    display['state'] = tk.NORMAL
    display.delete(0, 'end')
    display.insert(0, value + operation)
    display['state'] = tk.DISABLED


def calculate():  # Функция вычисляющая значение выражения в поле ввода
    value = display.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    display['state'] = tk.NORMAL
    display.delete(0, 'end')
    try:
        display.insert(0, eval(value))
        display['state'] = tk.DISABLED
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Вы ввели недопустимые символы. Нужно вводить только цифры.')
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!')

        display.insert(0, '0')


def clear():  # Функция очищает поле ввода
    value = display.get()
    if value != '':
        display['state'] = tk.NORMAL
        display.delete(0, 'end')
        display.insert(0, '0')
        display['state'] = tk.DISABLED


def make_digit_button(digit):  # Создание кнопок с цифрами
    return tk.Button(text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))


def make_operation_button(operation):  # Создание кнопок с операциями
    return tk.Button(text=operation, bd=5, font=('Arial', 20), fg='red', command=lambda: add_operation(operation))


def make_calc_button(operation):  # Создание кнопки вычисления ('=')
    return tk.Button(text=operation, bd=5, font=('Arial', 20), fg='red', command=calculate)


def make_clear_button(operation):  # Создание кнопки очистки поля ввода
    return tk.Button(text=operation, bd=5, font=('Arial', 20), fg='red', command=clear)


def press_key(event):  # Функция использования кнопок клавиатуры для ввода
    if event.char.isdigit():
        add_digit(event.char)
    if event.char in '+-*/':
        add_operation(event.char)
    if event.char == '"':
        calculate()


# Создание главного окна
win = tk.Tk()
win.title('Калькулятор')
win.geometry(f'250x280+100+200')
win['bg'] = '#ADD8E6'

win.bind('<Key>', press_key)

#   Создание поля ввода
display = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15, "bold"), width=15)
display.insert(0, '0')
display['state'] = tk.DISABLED
display.grid(row=0, column=0, columnspan=4, stic='wens', padx=5)

# Создание кнопок с цифрами
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

# Создание кнопок с операциями
make_operation_button('+').grid(row=1, column=3, stic="wens", padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stic="wens", padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stic="wens", padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stic="wens", padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stic="wens", padx=5, pady=5)
make_clear_button('c').grid(row=4, column=1, stic="wens", padx=5, pady=5)

# Установка размера колонок и столбцов
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
