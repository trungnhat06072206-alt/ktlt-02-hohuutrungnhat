# chương trình tìm các số nguyên tố trong khoảng từ 0 đến 100
num = 2     # bắt đầu từ 2 vì 0,1 khong phải là số nt
while num <= 100:
    is_prime = "true"
    i = 2
    while i * i <= num:  # chỉ cần kt đến căn bậc 2
        if num % i == 0:
            is_prime = "false"
            break
        i += 1
    if is_prime:
        print(num, end=" ")
    num += 1


