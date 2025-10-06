# ---------------------- BÀI 2 ----------------------
# Viết chương trình nhập nhiều tuple (name, age, score)
# rồi sắp xếp theo thứ tự name > age > score (tăng dần).

print("=== BÀI 2: SẮP XẾP TUPLE (name, age, score) ===")
print("Nhập dữ liệu theo định dạng: name, age, score (nhấn Enter để kết thúc)")

danh_sach = []

while True:
    du_lieu = input("Nhập tuple (hoặc nhấn Enter để dừng): ")
    if not du_lieu:
        break
    try:
        name, age, score = du_lieu.split(",")
        danh_sach.append((name.strip(), int(age.strip()), int(score.strip())))
    except:
        print("⚠️ Lỗi định dạng! Hãy nhập đúng dạng: name, age, score")

# Sắp xếp theo name > age > score
danh_sach.sort(key=lambda x: (x[0], x[1], x[2]))

print("\nKết quả sau khi sắp xếp:")
for item in danh_sach:
    print(item)
