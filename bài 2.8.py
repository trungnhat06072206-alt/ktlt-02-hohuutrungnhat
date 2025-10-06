# ---------------------- BÀI 1 ----------------------
# Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy,
# tạo ra một danh sách và một tuple chứa các số đó.

print("=== BÀI 1: CHUỖI SỐ -> LIST & TUPLE ===")

chuoi = input("Nhập các số, phân tách bằng dấu phẩy (,): ")

# Tách chuỗi thành danh sách các phần tử
ds = chuoi.split(",")
# Chuyển từng phần tử sang kiểu số nguyên
ds = [int(x.strip()) for x in ds]

# Tạo tuple từ danh sách
tp = tuple(ds)

print("Danh sách:", ds)
print("Tuple:", tp)
