from math import pi

while True:
    print("\n[1] Silindirin hacmini hesaplayınız\n[2] Koninin hacmini hesaplayınız\n[3] Kürenin hacmini hesaplayınız\n[4] Dikdörtgenler prizmasının hacmini hesaplayınız\n[5] Küpün hacmini hesaplayınız\n[X] Çıkış\n")
    secim = input("Yapmak istediğiniz işlemi giriniz: ")

    if secim == "1":
        try:
            r = int(input("r değerini giriniz: "))
            h = int(input("h değerini giriniz: "))
            print(2*pi*h*pow(r, 2))
        except ValueError:
            print("Lütfen geçerli bir değer giriniz...")
        continue

    elif secim == "2":
        try:
            r = int(input("r değerini giriniz: "))
            h = int(input("h değerini giriniz: "))
            print(1/3*h*pi*pow(r, 2))
        except ValueError:
            print("Lütfen geçerli bir değer giriniz...")
        continue

    elif secim == "3":
        try:
            r = int(input("r değerini giriniz: "))
            print(4/3*pi*pow(r, 3))
        except ValueError:
            print("Lütfen geçerli bir değer giriniz...")
        continue

    elif secim == "4":
        try:
            a = int(input("Taban birinci kenar giriniz: "))
            b = int(input("Taban ikinci kenar giriniz: "))
            h = int(input("h değerini giriniz: "))
            print(a*b*h)
        except ValueError:
            print("Lütfen geçerli bir değer giriniz...")
        continue

    elif secim == "5":
        try:
            a = int(input("Kenar uzunlugunu giriniz: "))
            print(pow(a, 3))
        except ValueError:
            print("Lütfen geçerli bir değer giriniz...")
        continue

    elif secim == "x" or secim == "X":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçerli bir seçim yapınız.")
        continue
    
    
