# Bài 1: Tìm các số chia hết cho 7 nhưng không phải bội số của 5 trong khoảng 2000-3200

result = []  # danh sách lưu các số thỏa mãn

for num in range(2000, 3201):  # 3201 vì range kết thúc trước số 3201
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))  # chuyển thành chuỗi để nối sau

# In ra kết quả trên 1 dòng, cách nhau bằng dấu phẩy
print(",".join(result))
