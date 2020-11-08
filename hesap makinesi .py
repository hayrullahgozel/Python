import math

def toplama(sayı1,sayı2):
    result = sayı1 + sayı2            # eger burada result ve prınt yapmasaydım buraya return yazacaktım ve asagıda 
    print(result)                     # print(toplama(deger1,deger2)) yazmalıydık.

def cıkarma(sayı1,sayı2):
    result = sayı1 - sayı2
    print(result)

def carpma(sayı1,sayı2):
    result = sayı1 * sayı2
    print(result)
        
def bolme(sayı1,sayı2):
    result = sayı1 / sayı2
    print(result)

def karekok(sayı1):
    return math.sqrt(sayı1)
    
def logaritma(sayı1):
    return math.log10(sayı1)

def faktoriyel(sayı1):
    return math.factorial(sayı1)               # bunu ve logarıtmayı return tarzında yazmamın sebebı asagıda prınt ıle işlem yaptıgım
    

    
while True : 

    deger1 = int(input("sayı 1 giriniz :"))
    deger2 = int(input("sayı 2 giriniz :")) 
    print("toplama = 1 ,cıkarma = 2 ,carpma = 3 ,bolme = 4 , logaritma = 5 , faktorıyel = 6 , karakök = 7")
    islem = int(input("yapmak istediginiz işlemi seçin : "))

    if islem == 1 :
        toplama(deger1,deger2)

    elif islem == 2 :
        cıkarma(deger1,deger2)

    if islem == 3 :
        carpma(deger1,deger2)

    if islem == 4 :
        bolme(deger1,deger2)

    if islem == 5 :
        print(f"ilk girilen degerin logarıtması : {logaritma(deger1) }")    # eger hem burada hemde def içinde prınt yaparsak none hatası alırız
        print(f"ikinci girilen degerin logarıtması : {logaritma(deger2) }")

    if islem == 6 :
        print(f"ilk girilen degerin faktoriyeli : {faktoriyel(deger1) }")    # eger hem burada hemde def içinde prınt yaparsak none hatası alırız (none)
        print(f"ikinci girilen degerin faktoriyeli : {faktoriyel(deger2) }")

    if islem == 7 :
        print(f"ilk girilen degerin karekök ü : {round(karekok(deger1),2) }")    # burada round kalıbı round(sayı,2) yaparasak virgülden sonra 2 basamak alır.
        print(f"ikinci girilen degerin karekök ü : {round(karekok(deger2),2) }")

    else :
        print("hatalı bır deger girdiniz...")
