
import requests



def dovizHesapla(miktar,bozdurulacakDoviz):
    try:
        url = 'https://api.genelpara.com/embed/para-birimleri.json'
        response=requests.get(url).json()
        toplam=float(response[bozdurulacakDoviz.upper()]["satis"])*int(miktar)
        print(f"Bozdurmak istediğiniz {bozdurulacakDoviz} karşılığı {toplam} TL'dir ")
    except:
        print("Bilgileri Yanlış Girdiniz...")

if __name__=="__main__":
    while True:
        print("Döviz Bozdurma Programına Hoşgeldiniz...\n1.Bozdurulacak Dövizi Hesapla\n2.Çıkış\n")
        secim=input("Seçiminiz: ")
        if secim=="2":
            break
        elif secim=="1":
            dovizCinsi=input("Bozdurulacak Döviz Cinsinin Kodunu Giriniz: ")
            tutar=input("Bozdurulacak Tutarı Giriniz: ")
            dovizHesapla(tutar,dovizCinsi)
            
        else:
            print("Yanlış Bir tuşlama Yaptınız...")
