import requests
import json

while True :
    print("Çıkmak için Q ya basın")
    sehir_sorgu = input("Hava durumu bilgisi istenilen şehir :")
    if sehir_sorgu == 'q' :
        print("Çıkış yapılıyor....")
        break

    url_adresi = "http://api.openweathermap.org/data/2.5/weather?q="

    result = requests.get(url_adresi + sehir_sorgu + "&appid=fd946ac95d025b328688360fad120ef2")  # burada şehiri belirlemek için orjinal url yı bozdum

    result = json.loads(result.text) # burada json ile parcalayıp içerisinden istedıgımı alabılecegım hale getiridim

    print(f"{sehir_sorgu} hava bilgisi\nSıcaklık : {result['main']['temp']-273} *C\nBulut Oranı : %{result['clouds']['all']}\nNem Oranı : {result['main']['humidity']}")
    print(f"Rüzgar hızı ve Baş bilgisi : {result['wind']['speed']} km/s / {result['wind']['deg']}")


#BİLGİLER OPENWEATER SAYFASINDAN ALINMIŞTIR.