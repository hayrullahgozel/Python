


def asalbulma(sayi1,sayi2):
    for sayi in range(sayi1, sayi2+1):         # burada ilk olarak atamış oldugumuz iki sayı arasında for ıle taramaya basladık 
        if sayi > 1 :         #burada ise 1 asal olmadıgı için 2 den baslayarak almasını sagladık aynı zamanda sayi degeri sayi1 ve sayi 2 arasındaki tüm degerler.
            for i in range(2,sayi):  # burada ise 2 den baslayarak tanımlanan butun sayıları sırayla dolastık
                if sayi%i == 0 :    # dolastıgımız bu sayılardan eger bir böleni var ise asal sayı degildir ve direk if dongusu içindekini durdurup digerr duruma baslaarız bastan for dongusu ıle
                    break    
            else:              # burası for dongusunun else kısmı
                print(sayi)     # eger for un içindekı ıf degerıne gırmez ıse else degerıne gırıp dırek sayıyı yazdıracak. 


sayi1 = int(input("sayı1 giriniz:"))
sayi2 = int(input("sayı2  giriniz:"))

asalbulma(sayi1,sayi2)
