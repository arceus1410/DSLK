class Ngay:
    def __init__(self, ngay: int, thang: int, nam: int):
        self.ngay = int(ngay)
        self.thang = int(thang)
        self.nam = int(nam)
        
class SinhVien:
    def __init__(self, maSV: str, ten: str, gioitinh: str, ngaysinh: Ngay, diachi: str, lop: str, khoa: str):
         self.maSV = int(maSV)
         self.ten = ten
         self.gioitinh = gioitinh
         self.ngaysinh = ngaysinh
         self.diachi = diachi
         self.khoa = khoa
         self.lop = lop
         

class Node:
    def __init__(self, data = None, next =None ):
        self.data = data
        self.next = next

def sapxepSv(first, data: SinhVien):
    temp = Node()
    current = temp
    element = Node(data)
    
    if first is None:
        first = element
        return first
    else:
        temp.next = first
        while current.next and current.next.data.maSV < element.data.maSV:
            current = current.next
            element.next = current.next
            current.next = element
    return temp.next

def taoList():
    n = int(input("so luong sinh vien: "))
    first = None
    
    for i in range(n):
        maSV = input(" ma so sv: ")
        ten = input(" ho va ten: ")
        gioitinh = input(" gioi tinh: ")
        ngay, thang, nam = input (" ngay thang nam sinh: ").split("/")
        ngaysinh = Ngay(ngay, thang, nam)
        diachi = input(" dia chi")
        lop = input(" lop: ")
        khoa = input(" khoa: ")
        data = SinhVien(maSV, ten, gioitinh, ngaysinh, diachi, lop, khoa)
        first = sapxepSv(first, data)
    return first
def printData(data):
    print(data.maSv + "\n")
    print(data.ten + "\n")
    print(data.gioitinh + "\n")
    print(data.ngaysinh.ngay + "/" + data.ngaysinh.thang + "/" + data.ngaysinh.nam + "\n" )
    print(data.diachi + "\n")
    print(data.lop + "\n")
    print(data.khoa)
    
def printlist(first):
    p = first
    while p:
        printData(p.data)
        p= p.next
        
def trungNgay(first):
     NgaySinh = []
     trung = []
     p = first
     while p:
         if p.data.ngaysinh.ngay not in NgaySinh:
             NgaySinh.append(p.data.ngaysinh.ngay)
         elif p.data.ngaysinh.ngay not in trung:
            trung.append(p.data.ngaysinh.ngay)
         p = p.next
     return trung 
 
def printTrungNgay(first):
     trung = trungNgay(first)
     if len(trung) == 0:
         print(" khong co sinh vien trung ngay sinh")
         return -1
     for i in range(len(trung)):
         p= first
         while p:
             if p.data.ngaysinh.ngay == trung[i]:
                 print(p.data.name +"\n")
             p =p.next 
def xoaSv(first):
    if first is None:
        return None
    trung = trungNgay(first)
    if len(trung) == 0:
        return first
    p = first
    while p:
        if p.next.ngaysinh.ngay in trung:
            if p.next.next:
                p.next = p.next.next
            else:
                p.next = None
                break
        else:
            p= p.next
    if first.data.ngaysinh.ngay in trung:
        first = first.next
    return first

        
        
        
def main():
    first = taoList()
    print(" sap xep sinh vien theo ma so sv la"+ "\n")
    printlist(first)
    print("sinh vien trung ngay sinh la: ")
    printTrungNgay(first)
    first = xoaSv(first)
    print("list sv sau xoa la")
    printlist(first)

if __name__ == "__main__":
    main()
        
            

        