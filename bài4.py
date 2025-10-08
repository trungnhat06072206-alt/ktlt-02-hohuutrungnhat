
# ----------------- PHẦN 1 -----------------
class Nguoi:
    """Lớp cha đại diện cho con người."""
    def getGender(self):
        return "Không xác định"  # mặc định nếu không ghi đè


class Nam(Nguoi):
    """Lớp con đại diện cho nam."""
    def getGender(self):
        return "Nam"


class Nu(Nguoi):
    """Lớp con đại diện cho nữ."""
    def getGender(self):
        return "Nữ"


# ----------------- PHẦN 2 -----------------
class Shape:
    """Lớp cha đại diện cho hình học."""
    def area(self):
        """Phương thức tính diện tích (mặc định = 0)."""
        return 0


class Square(Shape):
    """Lớp con đại diện cho hình vuông."""
    def __init__(self, side):
        self.side = side

    def area(self):
        """Ghi đè phương thức area() để tính diện tích hình vuông."""
        return self.side ** 2


# ----------------- CHƯƠNG TRÌNH CHÍNH -----------------
def main():
    print("=== BÀI 1: CLASS NGUOI ===")
    n1 = Nam()
    n2 = Nu()
    print("Giới tính đối tượng 1:", n1.getGender())
    print("Giới tính đối tượng 2:", n2.getGender())

    print("\n=== BÀI 2: CLASS SHAPE & SQUARE ===")
    hinh1 = Shape()
    print("Diện tích mặc định của Shape:", hinh1.area())

    # Nhập chiều dài cạnh hình vuông
    try:
        canh = float(input("Nhập chiều dài cạnh hình vuông: "))
        hinh2 = Square(canh)
        print("Diện tích hình vuông:", hinh2.area())
    except ValueError:
        print("⚠️ Lỗi: Vui lòng nhập số hợp lệ!")


if __name__ == "__main__":
    main()
