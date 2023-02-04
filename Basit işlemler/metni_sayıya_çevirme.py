kelime_sayı = {
    "bir": 1, "iki": 2, "üç": 3, "dört": 4, "beş": 5, "altı": 6, "yedi": 7, "sekiz": 8, "dokuz": 9, "on": 10,
    "yirmi": 20, "otuz": 30, "kırk": 40, "elli": 50, "altmış": 60, "yetmiş": 70, "seksen": 80, "doksan": 90,
    "yüz": 100, "bin": 1000, "milyon": 1000000, "milyar": 1000000000
            }
sayı_kelime = {}

for i, j in kelime_sayı.items():
    sayı_kelime[j] = i

def kontrol(x):  # girilen cümlede sayı olup olmadığı kontrolü
    sayı2, sayı3 = [], []

    if x in sayı_kelime:
        return sayı_kelime[x]
    sayı = [int(i) for i in str(x)]
    uzunluk = len(sayı)
    for i in sayı:
        sayı2.append(i * (10 ** (uzunluk - 1)))
        uzunluk -= 1
    for i in sayı2:
        if len(str(i)) > 2:
            sayı3.append(int(str(i)[0]))
            sayı3.append(i // int(str(i)[0]))
        else:
            sayı3.append(i)
    sayı4 = ""
    for i in sayı3:
        if i in sayı_kelime:
            sayı4 += (sayı_kelime[i]) + " "
        else:
            continue
    return sayı4
print("""
Bu uygulama ile girilen cümlenin içerisindeki kelimeleri sayıya dönüştürebilirsiniz.
0 ile 1 trilyon arsındaki rakamları metne uyarlamayı sağlar.
Örnek Cümle: "su faturasına bin dört yüz seksen beş tl ödedim" - Çıktısı: Su faturasına 1,485 tl ödedim.
Örnek Cümle: "benim 451 milyar 329 milyon 812 bin 713 liram var" Çıktısı: Benim 451,329,812,713 liram var.
Önemli uyarı: Lütfen kelimeleri Türkçe kurallarına uyarak yazın.
Doğru yazımlar için uğrayabilirsiniz https://www.tdk.gov.tr/icerik/yazim-kurallari/sayilarin-yazilisi/
""")
çeviri = input("Çevirmek İstediğiniz Cümle: ")

kontrol_stringi = ""
x = ""  # asıl string
for i in çeviri:
    if i == "I":
        kontrol_stringi += "ı"
    elif i == "İ":
        kontrol_stringi += "i"
    else:
        kontrol_stringi += i.lower()

for i in kontrol_stringi.split():
    if i.isdigit():
        x += kontrol(i)
    else:
        x += i + " "
new_string = ""
ilk_yazılacak_string = []
son_yazılacak_string = []
parçalama_yüz = []
parçalama_bin = []
parçalama_milyon = []
parçalama_milyar = []
parçlanmış_string = x.split()
milyar_basamağı = 0
milyon_basamağı = 0
binler_basamağı = 0
yüzler_basamağı = 0
sayımız = []

# milyarlar basamağı
if "milyar" in parçlanmış_string:
    for i in parçlanmış_string:
        if i in kelime_sayı.keys():
            parçalama_milyar.append(i)
        elif i not in kelime_sayı.keys():
            ilk_yazılacak_string.append(i)
        if i == "milyar":
            break
    for i in parçalama_milyar:
        if i in parçlanmış_string:
            parçlanmış_string.remove(i)

    test_string_milyar = ""
    for i in parçalama_milyar:
        if i in kelime_sayı.keys():
            test_string_milyar += str(kelime_sayı[i]) + " "
        else:
            test_string_milyar += str(i) + " "
    test_string_milyar = test_string_milyar.split()
    test_string_milyar.remove("1000000000")

    if len(test_string_milyar) < 2:
        for i in test_string_milyar:
            if i.isdigit():
                milyar_basamağı += int(i)
    else:
        for i in range(1, len(test_string_milyar)):
            if test_string_milyar[i - 1].isdigit():
                if int(test_string_milyar[i - 1]) < int(test_string_milyar[i]):
                    milyar_basamağı += int(test_string_milyar[i - 1]) * int(test_string_milyar[i])
                    test_string_milyar.remove(test_string_milyar[i - 1])
                    test_string_milyar.remove(test_string_milyar[i - 1])
                    for i in test_string_milyar:
                        if i.isdigit():
                            milyar_basamağı += int(i)
                    break
                elif int(test_string_milyar[i - 1]) > int(test_string_milyar[i]):
                    for i in test_string_milyar:
                        if i.isdigit():
                            milyar_basamağı += int(i)
                    break
    for i in ilk_yazılacak_string:
        parçlanmış_string.remove(i)
milyar_basamağı *= 1000000000

# milyonlar basamağı
if "milyon" in parçlanmış_string:
    for i in parçlanmış_string:
        if i in kelime_sayı.keys():
            parçalama_milyon.append(i)
        elif i not in kelime_sayı.keys():
            ilk_yazılacak_string.append(i)
        if i == "milyon":
            break
    for i in parçalama_milyon:
        if i in parçlanmış_string:
            parçlanmış_string.remove(i)

    test_string_milyon = ""
    for i in parçalama_milyon:
        if i in kelime_sayı.keys():
            test_string_milyon += str(kelime_sayı[i]) + " "
        else:
            test_string_milyon += str(i) + " "
    test_string_milyon = test_string_milyon.split()
    test_string_milyon.remove("1000000")

    if len(test_string_milyon) < 2:
        for i in test_string_milyon:
            if i.isdigit():
                milyon_basamağı += int(i)
    else:
        for i in range(1, len(test_string_milyon)):
            if test_string_milyon[i - 1].isdigit():
                if int(test_string_milyon[i - 1]) < int(test_string_milyon[i]):
                    milyon_basamağı += int(test_string_milyon[i - 1]) * int(test_string_milyon[i])
                    test_string_milyon.remove(test_string_milyon[i - 1])
                    test_string_milyon.remove(test_string_milyon[i - 1])
                    for i in test_string_milyon:
                        if i.isdigit():
                            milyon_basamağı += int(i)
                    break
                elif int(test_string_milyon[i - 1]) > int(test_string_milyon[i]):
                    for i in test_string_milyon:
                        if i.isdigit():
                            milyon_basamağı += int(i)
                    break

    for i in ilk_yazılacak_string:
        if i in parçlanmış_string:
            parçlanmış_string.remove(i)
milyon_basamağı *= 1000000

# binler basamağı
if "bin" in parçlanmış_string:
    for i in parçlanmış_string:
        if i in kelime_sayı.keys():
            parçalama_bin.append(i)
        elif i not in kelime_sayı.keys():
            ilk_yazılacak_string.append(i)
        if i == "bin":
            break
    for i in parçalama_bin:
        if i in parçlanmış_string:
            parçlanmış_string.remove(i)

    test_string_bin = ""
    if len(parçalama_bin) == 1:
        binler_basamağı += 1
    for i in parçalama_bin:
        if i in kelime_sayı.keys():
            test_string_bin += str(kelime_sayı[i]) + " "
        else:
            test_string_bin += str(i) + " "
    test_string_bin = test_string_bin.split()
    test_string_bin.remove("1000")

    if len(test_string_bin) < 2:
        for i in test_string_bin:
            if i.isdigit():
                binler_basamağı += int(i)
    else:
        for i in range(1, len(test_string_bin)):
            if test_string_bin[i - 1].isdigit():
                if int(test_string_bin[i - 1]) < int(test_string_bin[i]):
                    binler_basamağı += int(test_string_bin[i - 1]) * int(test_string_bin[i])
                    test_string_bin.remove(test_string_bin[i - 1])
                    test_string_bin.remove(test_string_bin[i - 1])
                    for i in test_string_bin:
                        if i.isdigit():
                            binler_basamağı += int(i)
                    break
                elif int(test_string_bin[i - 1]) > int(test_string_bin[i]):
                    for i in test_string_bin:
                        if i.isdigit():
                            binler_basamağı += int(i)
                    break

    for i in ilk_yazılacak_string:
        if i in parçlanmış_string:
            parçlanmış_string.remove(i)
binler_basamağı *= 1000

# yüzler basamağı
if "yüz" in parçlanmış_string or "yüz" not in parçlanmış_string:
    for i in parçlanmış_string:
        if i in kelime_sayı.keys():
            parçalama_yüz.append(i)
        else:
            son_yazılacak_string.append(i)
    test_string_yüz = ""
    for i in parçalama_yüz:
        if i in kelime_sayı.keys():
            test_string_yüz += str(kelime_sayı[i]) + " "
        else:
            test_string_yüz += str(i) + " "
    test_string_yüz = test_string_yüz.split()
    if len(test_string_yüz) < 2:
        for i in test_string_yüz:
            if i.isdigit():
                yüzler_basamağı += int(i)
    else:
        for i in range(1, len(test_string_yüz)):
            if test_string_yüz[i - 1].isdigit():
                if int(test_string_yüz[i - 1]) < int(test_string_yüz[i]):
                    yüzler_basamağı += int(test_string_yüz[i - 1]) * int(test_string_yüz[i])
                    test_string_yüz.remove(test_string_yüz[i - 1])
                    test_string_yüz.remove(test_string_yüz[i - 1])
                    for i in test_string_yüz:
                        if i.isdigit():
                            yüzler_basamağı += int(i)
                    break
                elif int(test_string_yüz[i - 1]) > int(test_string_yüz[i]):
                    for i in test_string_yüz:
                        if i.isdigit():
                            yüzler_basamağı += int(i)
                    break
    for i in parçalama_yüz:
        if i in parçlanmış_string:
            parçlanmış_string.remove(i)

sayımız_ham = ""
sayımızın_virgüllü_hali = ""
sayımız_ham += str(int(milyar_basamağı + milyon_basamağı + binler_basamağı + yüzler_basamağı))
sayımız_ham = sayımız_ham[::-1]

for i in range(0, len(sayımız_ham), 3):
    sayımızın_virgüllü_hali += sayımız_ham[i:i+3] + ","
sayımızın_virgüllü_hali = sayımızın_virgüllü_hali[:-1]
sayımızın_virgüllü_hali = sayımızın_virgüllü_hali[::-1]
sayımız.append(sayımızın_virgüllü_hali)
ekrana_yazdır = ""

for i in (ilk_yazılacak_string + sayımız + son_yazılacak_string):
    ekrana_yazdır += i + " "
ekrana_yazdır = ekrana_yazdır.rstrip()  # en sağdaki boşluğu kaldırır

if ekrana_yazdır[-1] == ".":
    print("Çeviriniz:",ekrana_yazdır.capitalize())

elif ekrana_yazdır[-1].isdigit():
    print("Çeviriniz:", ekrana_yazdır)

else:
    print("Çeviriniz:", ekrana_yazdır.capitalize() + ".")