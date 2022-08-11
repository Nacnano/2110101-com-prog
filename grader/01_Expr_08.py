def sqrt_n_times(x, n):
    return x**(1/n)


def cube_root(y):
    # คืนค่าประมาณของรากที่สามของ y โดยใชวิธี ้ ที่เสมือนการกดปุ่มด้วยสูตร
    #
    # ข้อแนะน า: เรียกใชฟ้ ังกช์ ัน sqrt_n_times
    return sqrt_n_times(y,) * sqrt_n_times


def main():
    q = float(input())
    print(cube_root(q))


exec(input())  # DON'T remove this line
