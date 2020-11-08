"""

Soru=Girilen bir sayının asal olup olmadıgını bulunuz ?
** asal sayı olma kosulu 1 veya kendisine bolunebılen sayılara denir.

"""

print("GİRİLEN SAYININ ASAL OLUP OLMADIGINI BULMA :")

sayi = int(input('sayı: '))
asalmi = True                  # burada dogru veya yanlıs oldugunu kontrolunu saglıyorum

if sayi == 1:                  # burada 1 sayısının asal sayı olmadıgını belırttık
    asalmi = False

for i in range(2, sayi):       # burada 2 ve daha sonra gırdıgımız sayıya kadar butun sayılara bolunup bolunmedıgını kontrol eder
    if (sayi % i == 0):        # bu satırda eger kalan sıfıra eşit mi diye sorar
        asalmi = False         # bu satırda ise eger kalan 0 esit veriyorsa false eşitleyip programı kapatıyoruz
        break

if asalmi:                 # eger işlem basamagı yukarıdakı kosulları gecıp buraya true olarak geldiyse asal dır 
    print('sayı asaldır.')
else:                  # eger if degişkenine girmez ise asal degildir.
    print('sayı asal değildir.')
