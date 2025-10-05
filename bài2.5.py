# Bài 2: Dãy Fibonacci trong khoảng từ 0 đến 1000

a, b = 0, 1
fibonacci = [a]

while b <= 1000:
    fibonacci.append(b)
    a, b = b, a + b

# In ra các số Fibonacci trên 1 dòng, cách nhau bằng dấu phẩy
print(",".join(str(x) for x in fibonacci))
