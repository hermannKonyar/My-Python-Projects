
import requests


def bozulanDovizHesapla(miktar, bozdurulacakDoviz):
    try:
        url = 'https://api.genelpara.com/embed/para-birimleri.json'
        response = requests.get(url).json()
        toplam = float(response[bozdurulacakDoviz.upper()]["alis"])*int(miktar)
        print(
            f"Bozdurmak istediğiniz {bozdurulacakDoviz} karşılığı {toplam} TL'dir ")
    except:
        print("Bilgileri Yanlış Girdiniz...")


def alinanDovizHesapla(miktar, alinacakDoviz):
    try:
        url = 'https://api.genelpara.com/embed/para-birimleri.json'
        response = requests.get(url).json()
        toplam = float(response[alinacakDoviz.upper()]["satis"])*int(miktar)
        print(
            f"Almak istediğiniz {alinacakDoviz} karşılığı {toplam} TL vermeniz gerekmektedir ")
    except:
        print("Bilgileri Yanlış Girdiniz...")


if __name__ == "__main__":
    while True:
        print("Döviz Bozdurma ve Alma Programına Hoşgeldiniz...\n1.Bozdurulacak Dövizi Hesapla\n2.Alınmak İstenen Dövizi Hesapla\n3.Çıkış\n")
        secim = input("Seçiminiz: ")
        if secim == "3":
            break
        elif secim == "1":
            dovizCinsi = input("Bozdurulacak Döviz Cinsinin Kodunu Giriniz: ")
            tutar = input("Bozdurulacak Tutarı Giriniz: ")
            bozulanDovizHesapla(tutar, dovizCinsi)
        elif secim == "2":
            dovizCinsi = input("Alınacak Döviz Cinsinin Kodunu Giriniz: ")
            tutar = input("Alınacak Tutarı Giriniz: ")
            alinanDovizHesapla(tutar, dovizCinsi)

        else:
            print("Yanlış Bir tuşlama Yaptınız...")
