import json

def main():
    json_data = '''
    {
        "ten": "Giang",
        "tuoi": 25,
        "dia_chi": {
            "pho": "số nhà 21 , ngõ 162 Đông Thiên , Vĩnh Hưng ,Hoàng Mai",
            "thanh_pho": "Hà Nội"
        },
        "so_thich": ["đọc sách", "chơi thể thao", "du lịch"]
    }
    '''
    doi_tuong_python = json.loads(json_data)
    print("Đối tượng Python:", doi_tuong_python)

    print("Tên:", doi_tuong_python['ten'])
    print("Tuổi:", doi_tuong_python['tuoi'])
    print("Địa chỉ:", doi_tuong_python['dia_chi']['pho'], ",", doi_tuong_python['dia_chi']['thanh_pho'])
    print("Sở thích:", ", ".join(doi_tuong_python['so_thich']))

if __name__ == "__main__":
    main()
