"""Khao sat ba cau hinh Q1, Q2, Q3 trong mien phieu: d co dinh [1, 5, 10, 25, 50], S = 50, 100, 200.
Do: so cap (s, c) voi c <= s duoc thu trong bang (so_lan_thu), so buoc tham lam, so to xuat ra,
va kich thuoc hai mang f, truoc. Chi dem phep toan, khong do thoi gian.
Chay: python khao_sat.py"""
from doi_tien import doi_tham_lam, doi_it_to_nhat, truy_vet_tien

D = [1, 5, 10, 25, 50]
CAU_HINH = [("Q1", 50), ("Q2", 100), ("Q3", 200)]


def main():
    print("d =", D)
    print("%-4s %-5s %-12s %-12s %-12s %-14s %s" % (
        "Bo", "S", "so_lan_thu", "buoc tham lam", "so to", "o f + truoc", "m*(S+1)-sum(d)"))
    for ten, S in CAU_HINH:
        f, truoc, so_lan_thu = doi_it_to_nhat(D, S)
        _, so_buoc = doi_tham_lam(D, S)
        so_to = len(truy_vet_tien(S, truoc))
        du_doan = len(D) * (S + 1) - sum(D)
        print("%-4s %-5d %-12d %-12d %-12d %-14d %d" % (
            ten, S, so_lan_thu, so_buoc, so_to, 2 * (S + 1), du_doan))
        assert so_lan_thu == du_doan


if __name__ == "__main__":
    main()
