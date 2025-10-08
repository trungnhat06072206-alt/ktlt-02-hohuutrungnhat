
def to_uppercase(s: str) -> str:
    """Chuyển tất cả ký tự sang chữ hoa (dùng str.upper())."""
    return s.upper()

def main():
    text = input("Bài 2 — Nhập chuỗi cần chuyển sang chữ hoa:\n")
    if text == "":
        print("Bạn chưa nhập gì.")
        return
    print("Kết quả:")
    print(to_uppercase(text))

if __name__ == "__main__":
    main()
