class Ngay:
    def __init__(self, ngay=1, thang=1, nam=2024):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam
    def display(self):
        print(f"Ngày: {self.ngay:02d}/{self.thang:02d}/{self.nam}")

    def so_ngay_trong_thang(self, thang, nam):
        if thang in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif thang in (4, 6, 9, 11):
            return 30
        elif thang == 2:
            return 29 if self.kiem_tra_nam_nhuan(nam) else 28
        return 0  

    def ngay_tiep_theo(self):
        self.ngay += 1
        if self.ngay > self.so_ngay_trong_thang(self.thang, self.nam):
            self.ngay = 1
            self.thang += 1
            if self.thang > 12:
                self.thang = 1
                self.nam += 1
def main():
    ngay = Ngay()
    ngay.display()
    ngay.ngay_tiep_theo()
    print("Ngày tiếp theo:")
    ngay.display()
    for i in range(5):
        ngay.ngay_tiep_theo()
        ngay.display()
main()