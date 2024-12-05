print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
import math
def Tinh (R):
    if R <= 0:
        print ("Bán kính không hợp lệ. Vui lòng nhập một giá trị khác")
        return

    chu_vi = 2*math.pi*R
    dien_tich = math.pi*R**2

    print("Chu vi hình tròn là:", chu_vi)
    print("Diện tích hình tròn là:", dien_tich)

ban_kinh = float(input("Nhập bán kinh hình tròn: "))

Tinh(ban_kinh)
