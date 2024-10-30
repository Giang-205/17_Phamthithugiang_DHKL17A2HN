import json

def main():
    doi_tuong_python = {
        "ten": "Giang",
        "tuoi": 25,
        "dia_chi": {
            "pho": "số nhà 21 , ngõ 162 Đông Thiên , Vĩnh Hưng ,Hoàng Mai",
            "thanh_pho": "Hà Nội"
        },
        "so_thich": ["đọc sách", "chơi thể thao", "du lịch"]
    }

    chuoi_json = json.dumps(doi_tuong_python, ensure_ascii=False, indent=4)
    print("Chuỗi JSON:")
    print(chuoi_json)
    print("\nCác giá trị:")
    for key, value in doi_tuong_python.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
