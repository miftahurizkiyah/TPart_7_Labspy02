# Membuat Program Menampilkan status gaji karyawan

gaji = int(input("Masukan gaji : "))
berkeluarga = (False , True)[input("Sudah Berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False , True)[input("Punya Rumah? (Y/T)") == "Y"]

if gaji > 3000000 :
    print("Gaji Sudah diatas UMR")
    if berkeluarga:
        print("Wajib Ikutan Asuransi dan Menabung untuk pensiun")
    else:
        print("Tidak Perlu Ikutan Asuransi")
    if punya_rumah :
        print("wajib bayar pajak rumah : ")
    else :
        print("tidak wajib bayar pajak rumah")
else:
    print("Gaji belum UMR")

