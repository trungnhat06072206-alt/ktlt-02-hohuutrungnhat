
import sys
from math import prod

def factorial(n: int) -> int:
    """Trả về n!; n phải là số nguyên >= 0."""
    if n < 0:
        raise ValueError("Không thể tính giai thừa của số âm.")
    # Tính giai thừa theo tích
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def parse_numbers(s: str):
    """Phân tích chuỗi s thành list số nguyên. Hỗ trợ phân tách bằng dấu cách và dấu phẩy."""
    # thay mọi dấu phẩy bằng dấu cách rồi tách
    parts = s.replace(',', ' ').split()
    nums = []
    for p in parts:
        try:
            nums.append(int(p))
        except ValueError:
            # bỏ phần không phải số
            continue
    return nums

def main():
    print("Bài 1 — Tính giai thừa. Nhập các số (cách nhau dấu cách hoặc dấu phẩy):")
    user = sys.stdin.readline().strip()
    if not user:
        print("Không có dữ liệu đầu vào. Ví dụ: 5 3,7 0")
        return

    nums = parse_numbers(user)
    if not nums:
        print("Không tìm thấy số hợp lệ trong đầu vào.")
        return

    outputs = []
    for n in nums:
        try:
            outputs.append(str(factorial(n)))
        except ValueError as e:
            # nếu có số âm, ghi rõ thông tin thay vì crash
            outputs.append(f"ERR({n})")

    # in ra một dòng, phân tách bằng dấu phẩy (không có khoảng trắng sau dấu phẩy)
    print(','.join(outputs))

if __name__ == "__main__":
    main()
