def hitung_zakat(harta):
    # Zakat dihitung sebesar 2.5% dari total harta yang dimiliki
    zakat = harta * 0.025
    return zakat

def main():
    # Minta pengguna untuk memasukkan total harta
    try:
        harta = float(input("Masukkan total harta yang dimiliki: "))
        if harta < 0:
            print("Harta tidak boleh kurang dari 0 karena dianggap kikir.")
        else:
            # Hitung Zakat
            zakat = hitung_zakat(harta)
            print(f"Jumlah Zakat yang harus dibayar: {zakat:.2f}")
    except ValueError:
        print("Silakan masukkan nilai numerik yang valid.")

if __name__ == "__main__":
    main()￼Enter