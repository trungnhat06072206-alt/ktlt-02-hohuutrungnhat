# Bài 1: Tính a/b với xử lý ngoại lệ

try:
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))

    ket_qua = a / b
    print(f"Kết quả của {a} / {b} = {ket_qua}")

except ValueError:
    print("Lỗi: Vui lòng nhập giá trị là số nguyên!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except Exception as e:
    print("Đã xảy ra lỗi khác:", e)
