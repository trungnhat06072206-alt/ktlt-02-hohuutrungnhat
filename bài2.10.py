# ---------------------- BÀI 3 ----------------------
# Định nghĩa một hàm in dictionary chứa các key là số từ 1 đến 20
# và value là bình phương của chúng.

def tao_dict_1_20():
    d = {}
    for i in range(1, 21):
        d[i] = i * i
    return d

# Gọi hàm và in ra
ket_qua = tao_dict_1_20()
print("Dictionary chứa bình phương từ 1 đến 20:")
print(ket_qua)
