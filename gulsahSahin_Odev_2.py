import math


boy = float(input("Boyunuzu m cinsinden giriniz: "))
kilo = float(input("Kilonuzu kg cinsinden giriniz: "))
cinsiyet = input("Cinsiyetinizi giriniz (E/K): ")
yas = int(input("Yasınızı giriniz: "))

BYA = 0.20247 * math.pow(boy,0.725) * math.pow(kilo,0.425)
print("Beden Yüzey Alanı: {}".format(BYA))

BKI = kilo / math.pow(boy,2)
print("Beden Kütle İndeksi: {}".format(BKI))

# 1 m = 39.3700787 inch
binch = boy * 39.3700787
bcm = boy*100

if (cinsiyet == "K") :
    y1 = 45.5 + 2.3 * binch - 60
    y2 = bcm-100 + yas/10 * 0.8
    if (BKI<=17.5):
        y3 = "Anoreksi, aşırı zayıf, yüksek risk"
    elif(BKI>=17.5 and BKI<19.1):
        y3 = "Zayıf"
    elif(BKI>=19.1 and BKI<25.8):
        y3 = "Normal kilolu"
    elif(BKI>=25.8 and BKI<27.3):
        y3 = "Biraz fazla kilolu"
    elif(BKI>=27.3 and BKI<32.3):
        y3 = "Fazla kilolu"
    elif(BKI>=32.3 and BKI<34.9):
        y3 = "Çok fazla kilolu"
    elif(BKI>=35 and BKI<40):
        y3 = "Sağlık açısından yüksek riskli kilolu"
    elif(BKI>=40 and BKI<50):
        y3 = "Hastalıklı bir şekilde aşırı kilolu"
    elif(BKI>=50 and BKI<60):
        y3 = "Süper aşırı kilolu"

else : 
    y1 = 50 + 2.3 * binch - 60
    y2 = bcm-100 + yas/10 * 0.9
    if (BKI<=17.5):
        y3 = "Anoreksi, aşırı zayıf, yüksek risk"
    elif(BKI>=17.5 and BKI<20.7):
        y3 = "Zayıf"
    elif(BKI>=20.7 and BKI<26.4):
        y3 = "Normal kilolu"
    elif(BKI>=26.4 and BKI<27.8):
        y3 = "Biraz fazla kilolu"
    elif(BKI>=27.8 and BKI<31.1):
        y3 = "Fazla kilolu"
    elif(BKI>=31.1 and BKI<34.9):
        y3 = "Çok fazla kilolu"
    elif(BKI>=35 and BKI<40):
        y3 = "Sağlık açısından yüksek riskli kilolu"
    elif(BKI>=40 and BKI<50):
        y3 = "Hastalıklı bir şekilde aşırı kilolu"
    elif(BKI>=50 and BKI<60):
        y3 = "Süper aşırı kilolu"


if (BKI<=18.5) : 
    y4 = "Zayıf"
elif (18.5>=BKI and BKI<=24.9):
    y4 = "Normal"
elif (25>=BKI and BKI<=29.9):
    y4 = "Fazla kilolı"
elif (30>=BKI and BKI<=34.9):
    y4 = "I. derece obez"
elif (35>=BKI and BKI<=39.9):
    y4 = "II. derece obez"
else : 
    y4 = "III. derece morbid obez"


print("y1: {}\ny2: {}\ny3: {}\ny4: {}".format(y1,y2,y3,y4))



