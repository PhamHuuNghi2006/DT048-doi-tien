"""DT048 - Doi tien: so lua chon tham lam voi so to it nhat.

Sinh vien: Pham Huu Nghi - MSSV N24DCDT053 - Lop D24CQDT01-N
Giao trinh INT1306, Chuong 4, muc 4.2.2. Chi dung thu vien chuan.
Mien phieu: d co 1 den 8 menh gia nguyen duong khac nhau, moi gia tri <= 50; 0 <= S <= 200.
"""

INF = float("inf")
SO_MENH_GIA_TOI_DA = 8
MENH_GIA_TOI_DA = 50
S_TOI_DA = 200


def kiem_tra_dau_vao(d, S):
    """Nem ValueError neu d hoac S nam ngoai mien cua phieu."""
    if isinstance(S, bool) or not isinstance(S, int) or not 0 <= S <= S_TOI_DA:
        raise ValueError("S phai la so nguyen tu 0 den %d" % S_TOI_DA)
    if not isinstance(d, (list, tuple)) or not 1 <= len(d) <= SO_MENH_GIA_TOI_DA:
        raise ValueError("d phai co tu 1 den %d menh gia" % SO_MENH_GIA_TOI_DA)
    for c in d:
        if isinstance(c, bool) or not isinstance(c, int) or not 1 <= c <= MENH_GIA_TOI_DA:
            raise ValueError("moi menh gia phai la so nguyen tu 1 den %d" % MENH_GIA_TOI_DA)
    if len(set(d)) != len(d):
        raise ValueError("cac menh gia phai khac nhau")


def doi_tham_lam(d, S):
    """Tham lam: sap giam dan, chia nguyen va lay du.
    Tra ve (cach, so_buoc); cach la None neu con du (tham_lam_khong_du)."""
    kiem_tra_dau_vao(d, S)
    cach, con, so_buoc = [], S, 0
    for c in sorted(d, reverse=True):
        so_buoc += 1
        k, con = divmod(con, c)
        cach.extend([c] * k)
    return (cach if con == 0 else None), so_buoc


def doi_it_to_nhat(d, S):
    """Bang f[s] = so to it nhat tra dung s; truoc[s] = menh gia cuoi.
    f[0] = 0, cac so tien khac ban dau chua dat (INF). Chi cap nhat tu s - c da dat.
    Tra ve (f, truoc, so_lan_thu); so_lan_thu dem so cap (s, c) voi c <= s."""
    kiem_tra_dau_vao(d, S)
    f = [0] + [INF] * S
    truoc = [0] * (S + 1)
    so_lan_thu = 0
    cs = sorted(d)
    for s in range(1, S + 1):
        for c in cs:
            if c > s:
                break
            so_lan_thu += 1
            if f[s - c] != INF and f[s - c] + 1 < f[s]:
                f[s] = f[s - c] + 1
                truoc[s] = c
    return f, truoc, so_lan_thu


def truy_vet_tien(S, truoc):
    """Truy nguoc tu S theo truoc de lay mot cach doi toi uu.
    Tra ve None neu S chua dat (S > 0 va truoc[S] = 0)."""
    if S > 0 and truoc[S] == 0:
        return None
    cach, s = [], S
    while s > 0:
        cach.append(truoc[s])
        s -= truoc[s]
    return cach


def kiem_nghiem(d, S, cach):
    """Dung neu moi to thuoc d va tong bang S."""
    if cach is None:
        return False
    return all(x in d for x in cach) and sum(cach) == S


def ket_qua(d, S):
    """Chay hai cach, tra ve tu dien ket qua."""
    tl, _ = doi_tham_lam(d, S)
    f, truoc, _ = doi_it_to_nhat(d, S)
    toi_uu = truy_vet_tien(S, truoc)
    return {"cach_tham_lam": tl, "cach_toi_uu": toi_uu,
            "toi_thieu": None if toi_uu is None else f[S], "f": f, "truoc": truoc}
