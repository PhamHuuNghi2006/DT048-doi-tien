# DT048 - Doi tien: so lua chon tham lam voi so to it nhat

- Sinh vien: Pham Huu Nghi - MSSV N24DCDT053 - Lop D24CQDT01-N
- Ma de: DT048 - INT13185 Nhom 03
- Ngon ngu: Python 3, chi dung thu vien chuan

## Input / output
- Input: d gom 1 den 8 menh gia nguyen duong khac nhau, moi gia tri <= 50; S nguyen, 0 <= S <= 200.
- Output: tham_lam=<so to> hoac tham_lam_khong_du; toi_thieu=<so to>; cach_toi_uu=<day to> hoac khong_doi_duoc.
- Input ngoai mien bi tu choi voi thong bao "Input khong hop le".

## Lenh chay
    python chay_demo.py                 # hai vi du VD01 va VD02
    python chay_demo.py "1 3 4" 6       # truyen tham so
    python chay_demo.py --nhap          # nhap tu ban phim
    python test_doi_tien.py             # bo 12 ca kiem thu
    python khao_sat.py                  # khao sat ba cau hinh Q1 Q2 Q3

## Cau truc
    doi_tien.py        doi_tham_lam, doi_it_to_nhat, truy_vet_tien, kiem_nghiem, kiem_tra_dau_vao
    chay_demo.py       hai vi du va nhap ban phim
    khao_sat.py        dem phep toan ba cau hinh Q1 Q2 Q3
    test_doi_tien.py   12 ca (expected tinh tay, doi chieu bang BFS doc lap)
    docs/anh_ket_qua/  anh goc A01-A11
