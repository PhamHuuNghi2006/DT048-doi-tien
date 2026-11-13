"""Chay hai vi du hoac nhap du lieu tu ban phim.

  python chay_demo.py              # hai vi du VD01 va VD02
  python chay_demo.py --nhap       # nhap d va S tu ban phim
  python chay_demo.py "1 3 4" 6    # truyen tham so
"""
import sys
from doi_tien import kiem_tra_dau_vao, ket_qua, kiem_nghiem


def chay(d, S):
    kiem_tra_dau_vao(d, S)
    kq = ket_qua(d, S)
    print("d=%s; S=%d" % (d, S))
    if kq["cach_tham_lam"] is None:
        print("tham_lam_khong_du")
    else:
        print("tham_lam=%d; cach_tham_lam=%s" % (len(kq["cach_tham_lam"]), kq["cach_tham_lam"]))
    if kq["cach_toi_uu"] is None:
        print("khong_doi_duoc")
    else:
        print("toi_thieu=%d; cach_toi_uu=%s" % (kq["toi_thieu"], kq["cach_toi_uu"]))
        print("kiem_nghiem=%s" % kiem_nghiem(d, S, kq["cach_toi_uu"]))
    print("f    =", ["inf" if v == float("inf") else v for v in kq["f"]])
    print("truoc=", kq["truoc"])
    print()


def main():
    try:
        if len(sys.argv) == 3:
            chay([int(x) for x in sys.argv[1].split()], int(sys.argv[2]))
        elif "--nhap" in sys.argv:
            d = [int(x) for x in input("Nhap cac menh gia (cach nhau dau cach): ").split()]
            S = int(input("Nhap S: "))
            chay(d, S)
        else:
            print("=== VD01 ===")
            chay([1, 3, 4], 6)
            print("=== VD02 ===")
            chay([2, 4], 3)
    except ValueError as loi:
        print("Input khong hop le:", loi)


if __name__ == "__main__":
    main()
