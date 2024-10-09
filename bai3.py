class phanso:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        while True:
            self.tu_so = int(input("Nhập tử số: "))
            self.mau_so = int(input("Nhập mẫu số: "))
            if self.kiem_tra_hop_le():
                break
            print("Mẫu số không thể bằng 0! Vui lòng nhập lại.")

    def in_phan_so(self):
        print(f"Phân số: {self.tu_so}/{self.mau_so}")
def main():
    while True:
        phan_so = phanso()
        phan_so.nhap_phan_so()
        phan_so.in_phan_so()

        tiep_tuc = input("Bạn có muốn nhập thêm phân số khác? (y/n): ")
        if tiep_tuc.lower() != 'y':
            break
main()