"""Bo kiem thu DT048: 12 ca doc lap. Expected tinh tay truoc khi chay;
tham_do_bfs la bo giai doc lap (BFS theo so to) de doi chieu so to it nhat.
Chay: python test_doi_tien.py"""
import sys
from collections import deque
from doi_tien import (doi_tham_lam, doi_it_to_nhat, truy_vet_tien,
                      kiem_nghiem, kiem_tra_dau_vao)


def tham_do_bfs(d, S):
    khoang, hang = {0: 0}, deque([0])
    while hang:
        u = hang.popleft()
        for c in d:
            v = u + c
            if v <= S and v not in khoang:
                khoang[v] = khoang[u] + 1
                hang.append(v)
    return khoang.get(S)


# (ma ca, d, S, so to tham lam hoac None, so to toi uu hoac None) - expected tinh tay
CA = [
    ("VD01",   [1, 3, 4],            6,   3,    2),
    ("VD02",   [2, 4],               3,   None, None),
    ("TK01",   [1, 5, 12],           15,  4,    3),
    ("TK02",   [25, 1, 10, 5],       63,  6,    6),
    ("BIEN01", [1, 3, 4],            0,   0,    0),
    ("BIEN02", [3, 7, 10],           7,   1,    1),
    ("BIEN03", [1, 5, 10, 25, 50],   200, 4,    4),
    ("KT09",   [1, 5, 10],           18,  5,    5),
    ("KT10",   [5],                  15,  3,    3),
    ("KT11",   [2, 5],               6,   None, 3),
]


def chay_ca():
    kq, so_assert = [], 0
    for ma, d, S, e_tl, e_qd in CA:
        tl, _ = doi_tham_lam(d, S)
        f, truoc, _ = doi_it_to_nhat(d, S)
        qd = truy_vet_tien(S, truoc)
        a_tl = None if tl is None else len(tl)
        a_qd = None if qd is None else len(qd)
        ok = a_tl == e_tl and a_qd == e_qd
        so_assert += 2
        if qd is not None:
            ok = ok and kiem_nghiem(d, S, qd) and len(qd) == f[S]
            so_assert += 2
        if tl is not None:
            ok = ok and kiem_nghiem(d, S, tl)
            so_assert += 1
        ok = ok and tham_do_bfs(d, S) == e_qd
        so_assert += 1
        kq.append((ma, d, S, e_tl, e_qd, a_tl, a_qd, ok))
    return kq, so_assert


def ca_loi():
    """LOI01: moi input ngoai mien phai bi tu choi bang ValueError."""
    cac = [([1, 3, 4], -1), ([1, 3, 4], 201), ([], 5), ([0, 5], 10),
           ([51, 5], 10), ([3, 3], 6), ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10), ([1, 3], 2.5)]
    kq = []
    for d, S in cac:
        try:
            kiem_tra_dau_vao(d, S)
            kq.append(False)
        except ValueError:
            kq.append(True)
    return all(kq), kq


def ca_kiem_nghiem():
    """KT12: ham con kiem_nghiem voi d = [1, 3, 4], S = 6."""
    d, S = [1, 3, 4], 6
    cac = [([3, 3], True), ([4, 1], False), ([2, 4], False), (None, False)]
    got = [kiem_nghiem(d, S, c) for c, _ in cac]
    return got == [e for _, e in cac], got


def main():
    kq, so_assert = chay_ca()
    print("%-7s %-22s %-4s %-8s %-8s %-8s %-8s %s" % (
        "Ca", "d", "S", "TL exp", "TOU exp", "TL act", "TOU act", "KQ"))
    dat = 0
    for ma, d, S, e1, e2, a1, a2, ok in kq:
        print("%-7s %-22s %-4s %-8s %-8s %-8s %-8s %s" % (
            ma, d, S, e1, e2, a1, a2, "PASS" if ok else "FAIL"))
        dat += ok
    ok, got = ca_loi()
    print("%-7s %-22s %-4s exp=8 loi act=%s %s" % ("LOI01", "8 input ngoai mien", "-", got, "PASS" if ok else "FAIL"))
    dat += ok; so_assert += 8
    ok, got = ca_kiem_nghiem()
    print("%-7s %-22s %-4s exp=[T,F,F,F] act=%s %s" % ("KT12", "kiem_nghiem", 6, got, "PASS" if ok else "FAIL"))
    dat += ok; so_assert += 4
    tong = len(kq) + 2
    print("-" * 78)
    print("TONG KET: %d/%d ca PASS, %d FAIL, %d assert" % (dat, tong, tong - dat, so_assert))
    return 0 if dat == tong else 1


if __name__ == "__main__":
    sys.exit(main())
