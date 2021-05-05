import random as rnd


class Soru:
    def __init__(self, metin, puan, cevap):
        self.metin = metin
        self.puan = puan
        self.cevap = cevap

    @staticmethod
    def karisikSinavYap():
        sayac, puan = 0, 0
        while True:
            sayi = int(rnd.random() * 2)
            if sayi == 0:
                i = int(rnd.random() * len(coktanSecmeli.coktanSecmeliHavuz))
                if sayac + coktanSecmeli.coktanSecmeliHavuz[i].puan > 110:
                    continue
                print("**************")
                print(str(i) + ". indexte " +
                      coktanSecmeli.coktanSecmeliHavuz[i].metin)
                print("A." + coktanSecmeli.coktanSecmeliHavuz[i].aSikki + "\nB." + coktanSecmeli.coktanSecmeliHavuz[
                    i].bSikki +
                      "\nC." + coktanSecmeli.coktanSecmeliHavuz[i].cSikki + "\nD." + coktanSecmeli.coktanSecmeliHavuz[
                          i].dSikki)
                kullCevap = input("Cevap: ")
                print("**************")
                with open("Sınav.txt", "a", encoding="utf-8") as file:
                    file.write("\n**************\n")
                    file.write(str(i) + ". indexte " +
                               coktanSecmeli.coktanSecmeliHavuz[i].metin)
                    file.write(
                        "A." + coktanSecmeli.coktanSecmeliHavuz[i].aSikki + "\nB." + coktanSecmeli.coktanSecmeliHavuz[
                            i].bSikki +
                        "\nC." + coktanSecmeli.coktanSecmeliHavuz[i].cSikki + "\nD." + coktanSecmeli.coktanSecmeliHavuz[
                            i].dSikki)
                    file.write("\nCevap: " + kullCevap)
                    file.write("\n**************")

                sayac += coktanSecmeli.coktanSecmeliHavuz[i].puan
                print(sayac)
                if coktanSecmeli.coktanSecmeliHavuz[i].cevap == kullCevap:
                    puan += coktanSecmeli.coktanSecmeliHavuz[i].puan
                if sayac >= 100:
                    with open("Sınav.txt", "a", encoding="utf-8") as file:
                        file.write("Aldığınız Puan:" + str(puan))
                    print("Aldığınız Puan:", puan)
                    break
            if sayi == 1:
                i = int(rnd.random() * len(klasikSoru.klasikSoruHavuz))
                if sayac + klasikSoru.klasikSoruHavuz[i].puan > 110:
                    continue
                print("**************")
                print(str(i) + ". indexte " +
                      klasikSoru.klasikSoruHavuz[i].metin)
                kullCevap = input("Cevap: ")
                print("**************")
                with open("Sınav.txt", "a", encoding="utf-8") as file:
                    file.write("\n**************\n")
                    file.write(str(i) + ". indexte " +
                               klasikSoru.klasikSoruHavuz[i].metin)
                    file.write("\nCevap: " + kullCevap)
                    file.write("\n**************")

                sayac += klasikSoru.klasikSoruHavuz[i].puan
                print(sayac)
                if klasikSoru.klasikSoruHavuz[i].cevap == kullCevap:
                    puan += klasikSoru.klasikSoruHavuz[i].puan
                if sayac >= 100:
                    with open("Sınav.txt", "a", encoding="utf-8") as file:
                        file.write("\nAldığınız Puan:" + str(puan))
                    print("Aldığınız Puan:", puan)
                    break


class coktanSecmeli(Soru):
    coktanSecmeliHavuz = []

    def __init__(self, metin, puan, cevap, aSikki, bSikki, cSikki, dSikki):
        super().__init__(metin, puan, cevap)
        self.aSikki = aSikki
        self.bSikki = bSikki
        self.cSikki = cSikki
        self.dSikki = dSikki

    @classmethod
    def soruEkle(cls, metin, puan, cevap, aSikki, bSikki, cSikki, dSikki):
        coktanSecmeli.coktanSecmeliHavuz.append(
            cls(metin, puan, cevap, aSikki, bSikki, cSikki, dSikki))
        coktanSecmeli.coktanSecmeliHavuz.sort(
            key=lambda c: c.puan, reverse=False)

    @staticmethod
    def soruCikar(metin):
        soruVarmı = False
        coktanSecmeli.coktanSecmeliHavuz.sort(
            key=lambda c: c.puan, reverse=False)
        for i in coktanSecmeli.coktanSecmeliHavuz:
            if metin in i.metin:
                soruVarmı = True
                print("**************")
                print(str(coktanSecmeli.coktanSecmeliHavuz.index(i)) +
                      ". indexte " + i.metin)
                print("A." + i.aSikki + "\nB." + i.bSikki +
                      "\nC." + i.cSikki + "\nD." + i.dSikki)
                print("**************")
        while True:
            try:
                if soruVarmı:
                    kullCevap = int(input("Silmek istediğiniz sorunun indexini giriniz..."))
                    coktanSecmeli.coktanSecmeliHavuz.pop(kullCevap)
                break
            except:
                print("Yanlış bir tuşlama yaptınız....")
                continue
        if not soruVarmı:
            print("Aradığınız soru bulunamadı...")
        print(len(coktanSecmeli.coktanSecmeliHavuz))

    @staticmethod
    def sinavYap():
        puan = 0
        sayac = 0
        while True:
            i = int(rnd.random() * len(coktanSecmeli.coktanSecmeliHavuz))
            if sayac + coktanSecmeli.coktanSecmeliHavuz[i].puan > 110:
                continue
            print("**************")
            print(str(i) + ". indexte " +
                  coktanSecmeli.coktanSecmeliHavuz[i].metin)
            print("A." + coktanSecmeli.coktanSecmeliHavuz[i].aSikki + "\nB." + coktanSecmeli.coktanSecmeliHavuz[
                i].bSikki +
                  "\nC." + coktanSecmeli.coktanSecmeliHavuz[i].cSikki + "\nD." + coktanSecmeli.coktanSecmeliHavuz[
                      i].dSikki)
            kullCevap = input("Cevap: ")
            print("**************")
            with open("Sınav.txt", "a", encoding="utf-8") as file:
                file.write("\n**************\n")
                file.write(str(i) + ". indexte " +
                           coktanSecmeli.coktanSecmeliHavuz[i].metin)
                file.write(
                    "A." + coktanSecmeli.coktanSecmeliHavuz[i].aSikki + "\nB." + coktanSecmeli.coktanSecmeliHavuz[
                        i].bSikki +
                    "\nC." + coktanSecmeli.coktanSecmeliHavuz[i].cSikki + "\nD." + coktanSecmeli.coktanSecmeliHavuz[
                        i].dSikki)
                file.write("\nCevap: " + kullCevap)
                file.write("\n**************")

            sayac += coktanSecmeli.coktanSecmeliHavuz[i].puan
            print(sayac)
            if coktanSecmeli.coktanSecmeliHavuz[i].cevap == kullCevap:
                puan += coktanSecmeli.coktanSecmeliHavuz[i].puan
            if sayac >= 100:
                break
        with open("Sınav.txt", "a", encoding="utf-8") as file:
            file.write("Aldığınız Puan:" + str(puan))
        print("Aldığınız Puan:", puan)

    @classmethod
    def metineGoreSirala(cls):
        if len(coktanSecmeli.coktanSecmeliHavuz) < 1:
            print("Yeterli Soru Bulunmamaktadır...")
            return
        soruVarmi = False
        kullSecim = input("Listelenmek istenen soruyu giriniz: ")
        for i in coktanSecmeli.coktanSecmeliHavuz:
            if kullSecim in i.metin:
                soruVarmi = True
                print("**************")
                print(str(coktanSecmeli.coktanSecmeliHavuz.index(i)) +
                      ". indexte " + i.metin)
                print("A." + i.aSikki + "\nB." + i.bSikki +
                      "\nC." + i.cSikki + "\nD." + i.dSikki)
                print("**************")
            if not soruVarmi:
                print("Aradığınız Soru Bulunamamıştır...")

    @classmethod
    def sikkaGoreSirala(cls):
        if len(coktanSecmeli.coktanSecmeliHavuz) < 1:
            print("Yeterli Soru Bulunmamaktadır...")
            return
        soruVarmi = False
        kullSecim = input("Listelenmek istenen soruyu giriniz: ")
        for i in coktanSecmeli.coktanSecmeliHavuz:
            if kullSecim in i.aSikki or kullSecim in i.bSikki or kullSecim in i.cSikki or kullSecim in i.dSikki:
                soruVarmi = True
                print("**************")
                print(str(coktanSecmeli.coktanSecmeliHavuz.index(i)) +
                      ". indexte " + i.metin)
                print("A." + i.aSikki + "\nB." + i.bSikki +
                      "\nC." + i.cSikki + "\nD." + i.dSikki)
                print("**************")
            if not soruVarmi:
                print("Aradığınız Soru Bulunamamıştır...")


class klasikSoru(Soru):
    klasikSoruHavuz = []

    def __ini__(self, metin, puan, cevap):
        super().__init__(metin, puan, cevap)

    @classmethod
    def soruEkle(cls, metin, puan, cevap):
        klasikSoru.klasikSoruHavuz.append(cls(metin, puan, cevap))

    @staticmethod
    def soruCikar(metin):
        soruVarmi = False
        klasikSoru.klasikSoruHavuz.sort(
            key=lambda c: c.puan, reverse=False)
        for i in klasikSoru.klasikSoruHavuz:
            if metin in i.metin:
                soruVarmi = True
                print("**************")
                print(str(klasikSoru.klasikSoruHavuz.index(i)) +
                      ". indexte " + i.metin)
                print("Cevap: " + i.cevap + "\nPuan: " + str(i.puan))
                print("**************")
        while True:
            try:
                if not soruVarmi:
                    print("Aradığınız soru bulunamamıştır...")
                    break
                kullCevap = int(input("Silmek istediğiniz sorunun indexini giriniz..."))
                klasikSoru.klasikSoruHavuz.pop(kullCevap)
                break
            except:
                print("Yanlış bir tuşlama yaptınız....")
                continue

    @classmethod
    def soruyaGoreSirala(cls):
        if len(klasikSoru.klasikSoruHavuz) < 1:
            print("Yeterli Soru Bulunmamaktadır...")
            return
        soruVarmi = False
        kullSecim = input("Listelenmek istenen soruyu giriniz: ")
        for i in klasikSoru.klasikSoruHavuz:
            if kullSecim in i.metin:
                soruVarmi = True
                print("**************")
                print(str(klasikSoru.klasikSoruHavuz.index(i)) +
                      ". indexte " + i.metin)
                print("Cevap: " + i.metin + "\nPuan: " + str(i.puan))
                print("**************")
            if not soruVarmi:
                print("Aradığınız Soru Bulunamamıştır")

    @staticmethod
    def cevabaGoreSirala():
        if len(klasikSoru.klasikSoruHavuz) < 1:
            print("Yeterli Soru Bulunmamaktadır...")
            return
        soruVarmi = False
        kullSecim = input("Listelenmek istenen soruyu giriniz: ")
        for i in klasikSoru.klasikSoruHavuz:
            if kullSecim in i.cevap:
                soruVarmi = True
                print("**************")
                print(str(klasikSoru.klasikSoruHavuz.index(i)) +
                      ". indexte " + i.metin)
                print("Cevap: " + i.metin + "\nPuan: " + str(i.puan))
                print("**************")
        if not soruVarmi:
            print("Aradığınız Soru Bulunamamıştır")

    @classmethod
    def sinavYap(cls):
        puan = 0
        sayac = 0
        while True:
            i = int(rnd.random() * len(klasikSoru.klasikSoruHavuz))
            if sayac + klasikSoru.klasikSoruHavuz[i].puan > 110:
                continue
            print("**************")
            print(str(i) + ". indexte " +
                  klasikSoru.klasikSoruHavuz[i].metin)
            kullCevap = input("Cevap: ")
            print("**************")
            with open("Sınav.txt", "a", encoding="utf-8") as file:
                file.write("\n**************\n")
                file.write(str(i) + ". indexte " +
                           klasikSoru.klasikSoruHavuz[i].metin)
                file.write("\nCevap: " + kullCevap)
                file.write("\n**************")

            sayac += klasikSoru.klasikSoruHavuz[i].puan
            print(sayac)
            if klasikSoru.klasikSoruHavuz[i].cevap == kullCevap:
                puan += klasikSoru.klasikSoruHavuz[i].puan
            if sayac >= 100:
                break
        with open("Sınav.txt", "a", encoding="utf-8") as file:
            file.write("\nAldığınız Puan:" + str(puan))
        print("Aldığınız Puan:", puan)


if __name__ == "__main__":
    while True:
        print(
            "***********\nSoru Bankası Uygulamamıza Hoş Geldiniz\n***********\n1.Soru Ekle\n2.Soru Çıkar\n3.Soru Listele\n4.Sınav Yap\n5.Çıkış Yap\n")
        try:
            kullSecim1 = int(input("Seçiminiz: "))
            if kullSecim1 == 1:
                while True:
                    try:
                        print("1.Çoktan Seçmeli Soru Ekle\n2.Klasik Soru Ekle\n3.Üst Menüye Dön\n")
                        kullSecim = int(input("Seçiminiz: "))
                        if kullSecim == 1:
                            while True:
                                try:
                                    soru = input("Soru Metnini Giriniz: ")
                                    cevap = input("Doğru Cevabı Giriniz: ")
                                    aSikki = input("A Şıkkını Giriniz: ")
                                    bSikki = input("B Şıkkını Giriniz: ")
                                    cSikki = input("C Şıkkını Giriniz: ")
                                    dSikki = input("D Şıkkını Giriniz: ")
                                    puan = int(input("Puanı Giriniz: "))
                                    if not aSikki in cevap and not bSikki in cevap and not cSikki in cevap and not dSikki in cevap:
                                        print("Cevap Şıklarda Yok Tekrar Soruyu Giriniz...")
                                        continue
                                    coktanSecmeli.soruEkle(soru, puan, cevap, aSikki, bSikki, cSikki, dSikki)
                                    kullSecim = input(
                                        "Tekrar Eklemek İçin Herhangi Bir Tuşa,Çıkmak İçin 0'ı Tuşlayınız...")
                                    if kullSecim == "0":
                                        break
                                    else:
                                        continue
                                except:
                                    print("Hatalı Bir Şey Girdiniz...")
                                    continue
                        elif kullSecim == 2:
                            while True:
                                try:
                                    soru = input("Soru Metnini Giriniz: ")
                                    cevap = input("Doğru Cevabı Giriniz: ")
                                    puan = int(input("Puanı Giriniz: "))
                                    klasikSoru.soruEkle(soru, puan, cevap)
                                    kullSecim = input(
                                        "Tekrar Eklemek İçin Herhangi Bir Tuşa,Çıkmak İçin 0'ı Tuşlayınız...")
                                    if kullSecim == "0":
                                        print(len(klasikSoru.klasikSoruHavuz))
                                        break
                                    else:
                                        continue
                                except:
                                    print("Hatalı Bir Şey Girdiniz...")
                                    continue
                        elif kullSecim == 3:
                            break
                        else:
                            print("Yanlış Bir Tuşlama Yaptınız...")
                            continue
                    except:
                        print("Yanlış Bir Giriş Yaptınız....")
                        continue
            elif kullSecim1 == 2:
                while True:
                    print("1.Çoktan Seçmeli Soru Çıkar\n2.Klasik Soru Çıkar\n3.Üst Menüye Dön\n")
                    kullSecim = int(input("Seçiminiz: "))
                    if kullSecim == 1:
                        while True:
                            if len(coktanSecmeli.coktanSecmeliHavuz) < 1:
                                print("Havuzda Soru Yok!")
                                break
                            kullSecim = input("Silmek istediğiniz soruyu giriniz: ")
                            coktanSecmeli.soruCikar(kullSecim)
                            kullSecim = input("Üst menüye dönmek için 0,devam etmek için herhangi bir tuşa basınız...")
                            if kullSecim == "0":
                                break
                            else:
                                continue
                    elif kullSecim == 2:
                        while True:
                            if len(klasikSoru.klasikSoruHavuz) < 1:
                                print("Havuzda yeterli soru yok!!")
                                break
                            kullSecim = input("Silmek istediğiniz soruyu giriniz: ")
                            klasikSoru.soruCikar(kullSecim)
                            kullSecim = input("Üst menüye dönmek için 0,devam etmek için herhangi bir tuşa basınız...")
                            if kullSecim == "0":
                                break
                            else:
                                continue
                    elif kullSecim == 3:
                        break
                    else:
                        print("Yanlış bir tuşlama yaptınız...")
                        continue

            elif kullSecim1 == 3:
                while True:
                    print("1.Çoktan Seçmeli Soru Sırala\n2.Klasik Soru Sırala\n3.Üst Menüye Dön\n")
                    kullSecim = input("Seçiminiz: ")
                    if kullSecim == "1":
                        while True:
                            print("1.Soruya Göre Sırala\n2.Şıkka Göre Sırala\n3.Üst Menüye Dön\n")
                            kullSecim = input("Seçiminiz: ")
                            if kullSecim == "1":
                                coktanSecmeli.metineGoreSirala()
                            elif kullSecim == "2":
                                coktanSecmeli.sikkaGoreSirala()
                            elif kullSecim == "3":
                                break
                            else:
                                continue
                    elif kullSecim == "2":
                        while True:
                            print("1.Soruya Göre Sırala\n2.Cevaba Göre Sırala\n3.Üst Menüye Dön\n")
                            kullSecim = input("Seçiminiz: ")
                            if kullSecim == "1":
                                klasikSoru.soruyaGoreSirala()
                            elif kullSecim == "2":
                                klasikSoru.cevabaGoreSirala()
                            elif kullSecim == "3":
                                break
                            else:
                                continue
                    elif kullSecim == "3":
                        break
                    else:
                        continue

            elif kullSecim1 == 4:
                while True:
                    print("1.Çoktan Seçmeli Sınav Yap\n2.Klasik Sınav Yap\n3.Karışık Sınav Yap\n4.Üst Menüye Dön\n")
                    kullSecim = input("Seçiminiz: ")
                    if kullSecim == "1":
                        coktanSecmeli.sinavYap()
                    elif kullSecim == "2":
                        klasikSoru.sinavYap()
                    elif kullSecim == "3":
                        if len(coktanSecmeli.coktanSecmeliHavuz) < 3 and len(klasikSoru.klasikSoruHavuz) < 3:
                            print("Yeterli soru yok")
                            continue
                        Soru.karisikSinavYap()
                    elif kullSecim == "4":
                        break
                    else:
                        continue
            elif kullSecim1 == 5:
                break
            else:
                continue

        except:
            print("Yanlış Bir Tuşlama Yaptınız...")
