import math
class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Điểm({self.x}, {self.y})"
class Elip(Diem):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a 
        self.b = b 
    def dienTich(self):
        return math.pi * self.a * self.b
    def __str__(self):
        return f"Elip với tâm tại {super().__str__()}, bán trục lớn = {self.a}, bán trục nhỏ = {self.b}"
class DuongTron(Elip):
    def __init__(self, x, y, r):
        super().__init__(x, y, r, r)  # bán trục lớn và bán trục nhỏ đều bằng bán kính
        self.r = r
    def dienTich(self):
        return math.pi * self.r ** 2
    def __str__(self):
        return f"Đường tròn với tâm tại {super().__str__()}, bán kính = {self.r}"
def main():
    print("Chương trình quản lý hình học")
    # Nhập thông tin cho elip
    x = float(input("Nhập hoành độ của tâm elip: "))
    y = float(input("Nhập tung độ của tâm elip: "))
    a = float(input("Nhập bán trục lớn của elip: "))
    b = float(input("Nhập bán trục nhỏ của elip: "))
    elip = Elip(x, y, a, b)
    print(f"\nThông tin elip: {elip}")
    print(f"Diện tích elip: {elip.dienTich()}")
    # Nhập thông tin cho đường tròn
    r = float(input("\nNhập bán kính đường tròn: "))
    duong_tron = DuongTron(x, y, r)
    print(f"\nThông tin đường tròn: {duong_tron}")
    print(f"Diện tích đường tròn: {duong_tron.dienTich()}")

main()