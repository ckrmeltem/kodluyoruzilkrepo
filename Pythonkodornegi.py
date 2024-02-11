# Kullanıcıdan bir sayı girişi alalım
sayi = int(input("Lütfen bir sayı girin: "))

# Sayının pozitif, negatif ya da sıfır olduğunu kontrol edelim ve ekrana yazdıralım
if sayi > 0:
    print("Girdiğiniz sayı pozitif.")
elif sayi < 0:
    print("Girdiğiniz sayı negatif.")
else:
    print("Girdiğiniz sayı sıfır.")
