# Bài 2: Kiểm tra 3 cạnh có tạo thành tam giác không

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Các cạnh phải lớn hơn 0!")

    # Điều kiện tam giác
    if a + b > c and a + c > b and b + c > a:
        print("Ba cạnh tạo thành một tam giác hợp lệ.")
    else:
        print("Ba cạnh KHÔNG tạo thành tam giác hợp lệ.")

except ValueError as ve:
    print("Lỗi:", ve)
except Exception as e:
    print("Đã xảy ra lỗi khác:", e)
