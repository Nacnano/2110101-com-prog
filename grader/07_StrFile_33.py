def read_next(f):
    while True:
        t = f.readline()
        if len(t) == 0:  # ถ้าอ่านหมดแล้ว ออกจากวงวน
            break
        x = t.strip().split()  # ลบ blank ซ้ายขวา
        if len(x) == 2:  # แยกแล้วได้ 2 ส่วน --> ถูกต้อง ก็คืนผล
            return x[0], x[1]
    return "", ""  # แฟ้มหมดแล้ว คืนสตริงว่าง
