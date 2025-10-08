import tkinter as tk
from tkinter import messagebox

# Hàm tính toán
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
        input_text.set("")
        expression = ""

# Giao diện
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
expression = ""
input_text = tk.StringVar()

# Ô hiển thị
input_frame = tk.Frame(window)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, width=30, font=('Arial', 18), justify='right')
input_field.grid(row=0, column=0, ipady=10)

# Nút bấm
btn_frame = tk.Frame(window)
btn_frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        b = tk.Button(btn_frame, text=text, width=7, height=2, command=btn_equal)
    else:
        b = tk.Button(btn_frame, text=text, width=7, height=2, command=lambda t=text: btn_click(t))
    b.grid(row=row, column=col, padx=5, pady=5)

# Nút xóa
clear_btn = tk.Button(window, text="C", width=33, height=2, command=btn_clear)
clear_btn.pack(pady=5)

window.mainloop()
