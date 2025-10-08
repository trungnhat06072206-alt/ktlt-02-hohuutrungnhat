import tkinter as tk
from tkinter import messagebox

def on_click():
    messagebox.showinfo("Thông báo", f"Bạn chọn: {radio_var.get()}")

root = tk.Tk()
root.title("Welcome")
root.geometry("300x150")

radio_var = tk.StringVar(value="First")

tk.Label(root, text="Welcome").pack(pady=5)
tk.Radiobutton(root, text="First", variable=radio_var, value="First").pack()
tk.Radiobutton(root, text="Second", variable=radio_var, value="Second").pack()
tk.Radiobutton(root, text="Third", variable=radio_var, value="Third").pack()

tk.Button(root, text="Click Me", command=on_click).pack(pady=10)

root.mainloop()
