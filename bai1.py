class hinhchunhat:
    Dogcount = 0
    def _init_ (self,dai,rong):
        self._dai = dai
        self._rong=rong
    def thong_tin(self):
        self.dai = float(input("Nhap chieu dai:"))
        self.rong = float(input("Nhap chieu rong:"))
    def tinh_chu_vi(self):
        return (self.dai + self.rong) *2
    def tinh_dien_tich(self):
        return self.dai * self.rong
    def in_thong_tin(self):
        chu_vi = self.tinh_chu_vi()
        dien_tich = self.tinh_dien_tich()
        print(f"Độ dài chiều dài : {self.dai}")
        print(f"Độ dài chiều rộng: {self.rong}")
        print(f"Chu vi hình chữ nhật: {chu_vi}")
        print(f"Diện tích hình chữ nhật: {dien_tich}")


# Tạo đối tượng hình chữ nhật và thực hiện các phương thức
hcn = hinhchunhat()
hcn.thong_tin()
hcn.in_thong_tin()