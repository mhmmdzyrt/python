#bir cümledeki sayıyı metne uyarlayan uygulama
print("""
Bu uygulama ile girilen cümlenin içerisindeki sayıları kelimelere dönüştürebilirsiniz.
0 ile 1 milyar arsındaki rakamları metne uyarlamayı sağlar.
Örnek: su faturasına 485 tl ödedim Çıktısı: Su faturasına dört yüz seksen beş tl ödedim.
""")
sayılar = {0: "sıfır", 1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz",
           10: "on", 20: "yirmi", 30: "otuz", 40: "kırk", 50: "elli", 60: "altmış", 70: "yetmiş", 80: "seksen",
           90: "doksan", 100: "yüz", 200: "iki yüz", 300: "üç yüz", 400: "dört yüz", 500: "beş yüz", 600: "altı yüz",
           700: "yedi yüz", 800: "sekiz yüz", 900: "dokuz yüz", 1000: "bin", 1000000: "milyon"
           }
değer1 = "256891654 adet ekmek ve 751 adet muz aldım"
değer = input("Cümlenizi ya da çevirmek istediğiniz sayıyı yazın: ")
dönüş_cümlemiz = ""
for x in değer.split(): # kullanıcıdan gelen veriyi aralarındaki boşluğa göre parçalıyıp döngüye sokuyoruz
    if x.isdigit(): # eğer stringte sayısal değer varsa
        if int(x) in sayılar.keys(): # sayılar sözlüğünün içinde olup olmadığını kontrol ediyoruz
            if int(x) == 1_000_000: # sayı 1 milyon iste sözlüte olduğu için başına bir ekliyoruz
                dönüş_cümlemiz += "Bir" + " " + sayılar[int(x)] + " "
            else:
                dönüş_cümlemiz += sayılar[int(x)] + " " # değer sözlükte varsa dönüş cümlemize yazdırıyoruz ör: 800
        else: # eğer sayılar sözlüğünde yoksa asıl işlemlere başlıyoruz ör: 15486
            onlar_basamağı = list() # sayının onlar basamağı için liste oluşturuyoruz
            binler_basamağı = list() # sayının yüzler basamağı için liste oluşturuyoruz
            milyonlar_basamağı = list() # sayının milyonlar basamağı için liste oluşturuyoruz
            bütün_basamaklar = list() # bütün basamakların birleştiği listemizi de oluşturduk
            temp_binler = int(len(x[-6:-3])) # sayının binler basamağınındaki indexi
            temp_onlar = int(len(x[-3:])) # sayının onlar basmağındaki indexi
            temp_milyon = int(len(x[:-6])) # sayının milyonlar basamağındaki indexi

            while True: # döngümüzü başlatma zamanı
                if len(x) <= 3: # eğer girilen sayının uzunluğu 3 ve daha az ise
                    for i in x: # sayıyı döngüye sokuyoruz
                        onlar_basamağı.append(int(i) * (10 ** (temp_onlar - 1)))  # sırası ile değerleri onlar basamagı
                                                                                  # listesine ekliyoruz
                        temp_onlar -= 1 # bir nevi çarpanlarına ayırıp tek tek yazırmak için temp değerini 1 azaltıyoruz
                                        # 846 için 800, 40 ve 6 değerini onlar basmağı listesine ekliyoruz
                    break # işlem birince döngüyü durduruyoruz
                if len(x) == 4: # girilen sayının uzunluğu 4 ise yukarıdaki işlemlerin benzerlerini tek tek uguluyoruz
                    for i in (x[:-3]):
                        if int(i) * (10 ** (temp_binler - 1)) == 1:
                            onlar_basamağı.append(10 ** 3)
                            continue
                        binler_basamağı.append(int(i) * (10 ** (temp_binler - 1)))
                        temp_binler -= 1
                        binler_basamağı.append(10 ** 3)
                    for i in x[-3:]:
                        onlar_basamağı.append(int(i) * (10 ** (temp_onlar - 1)))
                        temp_onlar -= 1
                    break
                if len(x) == 5: # girilen sayının uzunluğu 5 ise yukarıdakilere benzer işlemleri tek tek uguluyoruz
                    for i in (x[:-3]):
                        binler_basamağı.append(int(i) * (10 ** (temp_binler - 1)))
                        temp_binler -= 1
                    binler_basamağı.append(10 ** 3)
                    for i in x[-3:]:
                        onlar_basamağı.append(int(i) * (10 ** (temp_onlar - 1)))
                        temp_onlar -= 1
                    break
                if len(x) == 6: # girilen sayının uzunluğu 6 ise yukarıdakilere benzer işlemleri tek tek uguluyoruz
                    for i in (x[:-3]):
                        binler_basamağı.append(int(i) * (10 ** (temp_binler - 1)))
                        temp_binler -= 1
                    binler_basamağı.append(10 ** 3)
                    for i in x[-3:]:
                        onlar_basamağı.append(int(i) * (10 ** (temp_onlar - 1)))
                        temp_onlar -= 1
                    break

                if len(x) > 6:
                    for i in x[:-6]:
                        milyonlar_basamağı.append(int(i) * (10 ** (temp_milyon - 1)))
                        temp_milyon -= 1
                    milyonlar_basamağı.append(10 ** 6)
                    for i in (x[-6:-3]):
                        if (int(i) * (10 ** (temp_milyon - 1))) == 0:
                            binler_basamağı.append(int(i) * (10 ** (temp_binler - 1)))
                            temp_binler -= 1
                        elif (int(i) * (10 ** (temp_milyon - 1))) != 0:
                            binler_basamağı.append(int(i) * (10 ** (temp_binler - 1)))
                            temp_binler -= 1
                    for i in binler_basamağı:
                        if i > 0:
                            binler_basamağı.append(10 ** 3)
                            break
                    for i in x[-3:]:
                        onlar_basamağı.append(int(i) * (10 ** (temp_onlar - 1)))
                        temp_onlar -= 1
                    break
            bütün_basamaklar = milyonlar_basamağı + binler_basamağı + onlar_basamağı
            for i in bütün_basamaklar:
                if i == 0:
                    continue
                dönüş_cümlemiz += sayılar[i] + " "
    else:
        dönüş_cümlemiz += x + " "

dönüş_cümlemiz = dönüş_cümlemiz.rstrip()  # dönüştürdüğümüz cümlenin sonundaki boşluğu silmek için kod
if dönüş_cümlemiz[-1] == ".":  # kullanıcının girdiği cümlenin sonunda nokta olup olmadığını kontrol ediyoruz
    print("Çevriniz:",dönüş_cümlemiz.capitalize())  # nokta varsa eğer cümlenin başını büyük harfe çevirip yazdırıyoruz
else:  # sonunda nokta yoksa eğer nokta ekleyip baş harfi büyük yapıyoruz
    if dönüş_cümlemiz[0] == "i":
        print("Çeviriniz:", "İ" + dönüş_cümlemiz[1:] + ".")
    else:
        print("Çeviriniz:",dönüş_cümlemiz.capitalize()+".")
