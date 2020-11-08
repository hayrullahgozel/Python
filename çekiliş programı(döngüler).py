import random    # BURADA RANDOM U PROGRAMA TANITIYORUZ
while True :
    mylist = []                                # BURADA İÇERİSİNE EKLEMEK İÇİN BOŞ BİR LİSTE BELİRLEDİK

    kacisim=int(input("kaç isim ekleyeceksiniz :"))  
    x=0
    while x < kacisim :           # BURADA KAC TANE İSİM GİRECEGİMİZE GÖRE DONGUYU DONDERECEGİZ.
        isimler=str(input(f"lütfen {x+1} ci ismi giriniz :"))   #BURADA HER DONGUDE İSİM GİRMEMİZİ İSTEYECEK.
        mylist.append(isimler)       # BURADA HER DONGUDE GİRİLEN İSİMLERİ LİSTEYE EKLEYECEK
        x += 1     # DÖNGÜNÜN DÖNMESİ İÇİN X SIFIRKEN ONU BİR ARTTIRP TAKI BASTA BELİRTTİGİMİZ KAC İSİM SAYISNA KADAR ULAŞMASINA YARIYOR
    print("isim seçiliyor...")
    print(random.choice(mylist)) #SON OLARAK RANDOMLA HERHANGİ BİR DEGERİ SEÇİYORUZ.