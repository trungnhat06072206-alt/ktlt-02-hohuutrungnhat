
import hinhtron  # import module tự tạo
import random

def main():
    # Tạo ngẫu nhiên bán kính từ 10 → 100
    r = random.uniform(10, 100)
    print(f"Bán kính ngẫu nhiên: {r:.2f}")

    # Gọi hàm trong module hinhtron
    cv = hinhtron.chu_vi(r)
    dt = hinhtron.dien_tich(r)

    print(f"Chu vi hình tròn: {cv:.2f}")
    print(f"Diện tích hình tròn: {dt:.2f}")

if __name__ == "__main__":
    main()
