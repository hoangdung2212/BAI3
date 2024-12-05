print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
def benefit (t, n, k):
    tiền_nhận = n
    for month in range(k):
        tiền_nhận *= (1 + t / 100)

    return tiền_nhận

# Nhập lãi suất, số vốn ban đầu và số tháng gửi
t = float(input("Nhập lãi suất tiết kiệm (t%:"))
n = float(input("Nhập số vốn ban đầu (n):"))
k = int(input("Nhập số tháng gửi (k): "))

#Tính và in số tiền nhận được
số_tiền_nhận = benefit(t, n, k)
print (f"số tiền nhận được sau {k} tháng là: {số_tiền_nhận:.2f}")

