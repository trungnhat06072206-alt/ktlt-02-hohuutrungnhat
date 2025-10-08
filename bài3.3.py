
import random

def tao_so_ngau_nhien():
    """Hàm tạo một số thực ngẫu nhiên trong khoảng 10 → 100."""
    so = random.uniform(10, 100)  # uniform() cho số thực
    return round(so, 2)  # làm tròn 2 chữ số thập phân

def main():
    so = tao_so_ngau_nhien()
    print(f"Số thập phân ngẫu nhiên trong khoảng 10–100 là: {so}")

if __name__ == "__main__":
    main()
