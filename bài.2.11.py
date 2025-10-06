# ---------------------- BÀI 4 ----------------------
# Với số nguyên n, tạo ra dictionary chứa (i, i*i) với i từ 1 đến n.

n = int(input("Nhập số nguyên n: "))

d = {}
for i in range(1, n + 1):
    d[i] = i * i

print("Dictionary kết quả:")
print(d)
