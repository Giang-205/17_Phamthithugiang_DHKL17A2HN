import xml.dom.minidom

def main():

    doc = xml.dom.minidom.parse("bai2.3.xml")  

    print("Tên tài liệu:", doc.nodeName)
    print("Tên nút con đầu tiên:", doc.firstChild.tagName)

    danh_sach_nhan_vien = doc.getElementsByTagName("staff")
    print("%d nhân viên:" % danh_sach_nhan_vien.length)
    for nhan_vien in danh_sach_nhan_vien:
        ten = nhan_vien.getElementsByTagName("name")[0].firstChild.nodeValue
        print("Tên nhân viên:", ten)

if __name__ == "__main__":
    main()

