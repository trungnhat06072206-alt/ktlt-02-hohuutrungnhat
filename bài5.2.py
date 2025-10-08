import tkinter as tk
from tkinter import messagebox
import math

def giai_pt():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Giải phương trình
        if a == 0 and b == 0:
            result = "Phương trình vô nghiệm"
        elif a == 0:
            result = f"Phương trình bậc nhất: x = {-c / b:.2f}"
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                result = "Phương trình vô nghiệm"
            elif delta == 0:
                result = f"Phương trình có nghiệm kép: x = {-b / (2*a):.2f}"
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)
                result = f"x1 = {x1:.2f}, x2 = {x2:.2f}"

        messagebox.showinfo("Kết quả", result)

        # Ghi vào file
        with open("ketqua_pt.txt", "a", encoding="utf-8") as f:
            f.write(f"a={a}, b={b}, c={c} => {result}\n")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số!")

# GUI
root = tk.Tk()
root.title("Giải Phương Trình")
root.geometry("350x250")

tk.Label(root, text="Nhập a:").grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Nhập b:").grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Label(root, text="Nhập c:").grid(row=2, column=0, padx=10, pady=10)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

tk.Button(root, text="Giải phương trình", command=giai_pt).grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
