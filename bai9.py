class DaGiac:
    def __init__(self, canh):
        self.canh = canh
    def chuVi(self):
        return sum(self.canh)
class HinhBinhHanh(DaGiac):
    def __init__(self, day, cao):
        super().__init__([day, day, cao, cao])
        self.day = day
        self.cao = cao
    def dienTich(self):
        return self.day * self.cao
class HinhChuNhat(HinhBinhHanh):
    def __init__(self, rong, cao):
        super().__init__(rong, cao)
        self.rong = rong
        self.cao = cao
    def chuVi(self):
        return 2 * (self.rong + self.cao)
class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh
def main():
    print("Chương trình quản lý hình học")
    # Nhập hình chữ nhật
    rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    cao = float(input("Nhập chiều dài hình chữ nhật: "))
    hcn = HinhChuNhat(rong, cao)
    print(f"Chu vi hình chữ nhật: {hcn.chuVi()}")
    print(f"Diện tích hình chữ nhật: {hcn.dienTich()}")
    # Nhập hình bình hành
    day = float(input("\nNhập đáy hình bình hành: "))
    cao_bhh = float(input("Nhập chiều cao hình bình hành: "))
    hbh = HinhBinhHanh(day, cao_bhh)
    print(f"Chu vi hình bình hành: {hbh.chuVi()}")
    print(f"Diện tích hình bình hành: {hbh.dienTich()}")
    # Nhập hình vuông
    canh = float(input("\nNhập cạnh hình vuông: "))
    hv = HinhVuong(canh)
    print(f"Chu vi hình vuông: {hv.chuVi()}")
    print(f"Diện tích hình vuông: {hv.dienTich()}")
main()