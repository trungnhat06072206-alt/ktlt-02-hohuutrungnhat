import random

# Nhập độ dài danh sách
n = int(input("Nhập số phần tử của list A: "))
m = int(input("Nhập số phần tử của list B: "))

# Tạo list ngẫu nhiên trong khoảng [-100, 100]
A = [random.randint(-100, 100) for _ in range(n)]
B = [random.randint(-100, 100) for _ in range(m)]

# Ghép 2 list
C = A + B

print("\nList A:", A)
print("List B:", B)
print("List C (A + B):", C)

# Sắp xếp tăng dần
C.sort()
print("\nList C sau khi sắp xếp tăng dần:", C)

# Nhập và kiểm tra số x trong list C
x = int(input("\nNhập số nguyên x để kiểm tra: "))

if x in C:
    count = C.count(x)
    first_index = C.index(x)
    print(f"Số {x} xuất hiện {count} lần, vị trí đầu tiên là {first_index}.")
else:
    print(f"Số {x} không có trong list C.")

# Xóa các phần tử trùng lặp
C_unique = list(set(C))
C_unique.sort()

print("\nList C sau khi xóa phần tử trùng lặp:", C_unique)
