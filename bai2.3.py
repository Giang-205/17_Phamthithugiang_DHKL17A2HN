import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("bai2.3.xml") 

    company_name = doc.getElementsByTagName("name")[0].firstChild.nodeValue
    print("Tên công ty:", company_name)

    staff_elements = doc.getElementsByTagName("staff")
    print("%d nhân viên:" % staff_elements.length)
    for staff in staff_elements:
        name = staff.getElementsByTagName("name")[0].firstChild.nodeValue
        salary = staff.getElementsByTagName("salary")[0].firstChild.nodeValue
        print("Tên nhân viên:", name)
        print("Mức lương:", salary)
        print() 

if __name__ == "__main__":
    main()
