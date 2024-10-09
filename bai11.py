import math
class TamGiac:
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b  
        self.c = c  
    def chuVi(self):
        return self.a + self.b + self.c
    def dienTich(self):
        p = self.chuVi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def __str__(self):
        return f"Tam giác với các cạnh: a = {self.a}, b = {self.b}, c = {self.c}"
class TamGiacVuong(TamGiac):
    def __init__(self, canh_dai, canh_ngan):
        self.c = math.sqrt(canh_dai**2 + canh_ngan**2) 
        super().__init__(canh_dai, canh_ngan, self.c)
    def dienTich(self):
        return (self.a * self.b) / 2
    def __str__(self):
        return f"Tam giác vuông với cạnh dài = {self.a}, cạnh ngắn = {self.b}, cạnh huyền = {self.c:.2f}"
class TamGiacCan(TamGiac):
    def __init__(self, canh_bang, canh_khac):
        self.a = canh_bang
        self.b = canh_bang
        self.c = canh_khac
        super().__init__(self.a, self.b, self.c)
    def __str__(self):
        return f"Tam giác cân với các cạnh: a = {self.a}, b = {self.b}, c = {self.c}"
class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)
    def __str__(self):
        return f"Tam giác đều với cạnh = {self.a}"
def main():
    print("Chương trình quản lý tam giác")
    # Nhập tam giác thường
    a = float(input("Nhập cạnh a của tam giác: "))
    b = float(input("Nhập cạnh b của tam giác: "))
    c = float(input("Nhập cạnh c của tam giác: "))
    tam_giac = TamGiac(a, b, c)
    print(f"\nThông tin {tam_giac}")
    print(f"Chu vi tam giác: {tam_giac.chuVi()}")
    print(f"Diện tích tam giác: {tam_giac.dienTich()}")

    # Nhập tam giác vuông
    canh_dai = float(input("\nNhập cạnh dài của tam giác vuông: "))
    canh_ngan = float(input("Nhập cạnh ngắn của tam giác vuông: "))
    tam_giac_vuong = TamGiacVuong(canh_dai, canh_ngan)
    print(f"\nThông tin {tam_giac_vuong}")
    print(f"Chu vi tam giác vuông: {tam_giac_vuong.chuVi()}")
    print(f"Diện tích tam giác vuông: {tam_giac_vuong.dienTich()}")

    # Nhập tam giác cân
    canh_bang = float(input("\nNhập cạnh bằng của tam giác cân: "))
    canh_khac = float(input("Nhập cạnh khác của tam giác cân: "))
    tam_giac_can = TamGiacCan(canh_bang, canh_khac)
    print(f"\nThông tin {tam_giac_can}")
    print(f"Chu vi tam giác cân: {tam_giac_can.chuVi()}")
    print(f"Diện tích tam giác cân: {tam_giac_can.dienTich()}")

    # Nhập tam giác đều
    canh_deu = float(input("\nNhập cạnh của tam giác đều: "))
    tam_giac_deu = TamGiacDeu(canh_deu)
    print(f"\nThông tin {tam_giac_deu}")
    print(f"Chu vi tam giác đều: {tam_giac_deu.chuVi()}")
    print(f"Diện tích tam giác đều: {tam_giac_deu.dienTich()}")

main()