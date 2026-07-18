def kelime_frekansi_bul(metin):
    # Noktalama işaretlerini metinden temizliyoruz (Kelimeler temiz çıksın diye)
    noktalama_isaretleri = ".,:;!?\"'()*-+"
    temiz_metin = ""
    for karakter in metin:
        if karakter not in noktalama_isaretleri:
            temiz_metin = temiz_metin + karakter
    # Metni tamamen küçük harfe çevirip kelimelerine ayırıyoruz
    kelime_listesi = temiz_metin.lower().split()
    # Kelimelerin çetelesini tutacağımız boş sözlük
    frekans_sozlugu = {}
    # Kelimeleri çetele defterine işleme
    for kelime in kelime_listesi:
        if kelime in frekans_sozlugu:
            frekans_sozlugu[kelime] = frekans_sozlugu[kelime] + 1
        else:
            frekans_sozlugu[kelime] = 1
    # Sözlüğü en çok geçen kelimeden en aza doğru sıralama
    # .items() sözlüğü (kelime, sayı) çiftleri haline getirir
    # sorted() ve key=lambda ile sayısal değerlere (x[1]) göre tersten (reverse=True) sıralarız
    sirali_kelimeler = sorted(frekans_sozlugu.items(), key=lambda x: x[1], reverse=True)
    # En çok geçen ilk 5 kelimeyi dilimleme (slicing) ile alıyoruz
    en_cok_gecen_5 = sirali_kelimeler[:5]
    return en_cok_gecen_5

kullanici_metni = input("Lütfen analiz edilecek uzun metni giriniz = ")

sonuc = kelime_frekansi_bul(kullanici_metni)

print("Metinde en çok geçen 5 kelime = ")
# Sıralı listedeki (kelime, adet) ikililerini döngüyle ekrana basıyoruz
for kelime, adet in sonuc:
    print(f"'{kelime}' kelimesi {adet} kez geçiyor.")