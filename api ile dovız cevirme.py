import requests
import json

while True:
    adres = "https://api.exchangeratesapi.io/latest?base="


    print("dolar = USD \ntürk lirası =TRY\neuro = EUR\nrus rublesi = RUB\ndegerlerini giriniz..")


    bozulanDovız = input("lutfen bozdurmak istedgınız dovız kurunu gırınız : ")
    bozulanKur = input("lutfen bozdurulacak dovız kurunu gırınız : ")
    mıktar = int(input(f"Ne kadar { bozulanDovız } bozdurmak istiyorsunuz :  "))



    result = requests.get(adres + bozulanDovız)
    result = json.loads(result.text)

    print("1 {0} = {1} {2}".format(bozulanDovız, result["rates"][bozulanKur], bozulanKur))
    print("{0} {1} = {2} {3}".format(mıktar, bozulanKur, mıktar * result["rates"][bozulanKur],bozulanKur))