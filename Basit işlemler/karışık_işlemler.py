işlemler = """Program ile Yapabileceğiniz İşlemler:
1. Girdiğiniz Sayının Tek mi Çift mi Olup Olmadığını Bulma İşlemi
2. Girilen Sayının Armstrong Sayısı Olup Olmadığını Bulma işlemi
3. Girilen Sayıya Kadar Armstrong Sayıları Bulma işlemi
4. Girilen Sayının Asal Olup Olmadığını Bulma İşlemi
5. Girilen Sayıya Kadar Asal Sayıları Bulma İşlemi
6. Girilen Sayının Tam Bölenlerini bulma İşlemi
7. Fibonacci Sayısını Bulma İşlemi
8. Faktöriyel Serisi İşlemi
Herhangi Bir anda Programdan Sonlandırmak için "q"'ya Basın."""
print(işlemler)


# asal kontrolü
def check(prime):
    if prime == 1:
        return False
    if prime == 2:
        return True
    for i in range(2, int(prime ** 0.5) + 1):
        if prime % i == 0:
            return False
    return True


# faktoriyal bulma
def factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


# fibonacci serisi
def fibonacci(number):
    x = 1
    y = 1
    result = [0, 1, 1]
    for i in range(number):
        x, y = y, x + y

        result.append(y)
        if len(result) == number:
            break
    return result


# tam bölenleri bulma
def divide(number):
    result = []
    for i in range(1, int(number ** 0.5)):
        if number % i == 0:
            result.append(i)
            result.append(number // i)
    result.sort()
    return result


# tek mi çift mi kontrolü
def even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


# armstrong kontrol
def armstrong(number):
    result = 0
    if int(number) == 1 or int(number) == 0:
        return True
    if int(number) > 10:
        for i in str(number):
            result += (int(i) ** len(str(number)))
    if result == number:
        return True
    return False


seçim = ("1", "2", "3", "4", "5", "6", "7", "8", "q", "d")
girdi = input("\nLütfen İşleminizi Giriniz: ")
deneme = 3
while True:
    if girdi not in seçim:
        print("\nLütfen Geçerli Bir İşlem Giriniz!\n")
        deneme -= 1
        print(deneme, "deneme hakkınız kaldı!\n")
        if deneme == 0:
            print("Program Sonlandırıldı..")
            break
        else:
            girdi = input("Lütfen İşleminizi Giriniz: ")

    elif girdi in seçim:
        deneme = 3
        if girdi == "q":
            print("\nProgram Sonlandırıldı.")
            break
        # tek mi çift mi işlemi:
        if girdi == "1":
            sayı = input(
                "Şu anki İşlemi değiştirmek için d'ye basın. \nTek mi çift mi? Öğrenmek İçin: \n\nSayıyı Girin: ")
            if sayı.isdigit():
                sayı_virgüllü = ""
                for i in range(0, len(sayı), 3):
                    sayı_virgüllü += sayı[::-1][i:i + 3] + ","
                sayı_virgüllü = sayı_virgüllü[::-1]
                if even_odd(int(sayı)):
                    print("\n> {} Çift Sayıdır.\n".format(sayı_virgüllü[1:]))
                else:
                    print("\n> {} Tek Sayıdır.\n".format(sayı))
            elif sayı == "q":
                print("Program Sonlandırıldı.")
                break
            elif sayı == "d":
                print(işlemler)
                girdi = input("\nLütfen İşleminizi Giriniz: ")

            else:
                print("\nLütfen Sadece Sayı Giriniz.\n")

        # armstrong sayısı olup olmadığı:
        if girdi == "2":
            sayı = input(
                "Şu anki İşlemi değiştirmek için d'ye basın. \nArmstrong mu? Öğrenmek İçin: \n\nSayıyı Girin: ")
            if sayı.isdigit():
                if armstrong(int(sayı)):
                    print("{} armstrong bir sayıdır.".format(sayı))
                else:
                    print("{} armstrong bir sayı değildir.".format(sayı))
            elif sayı == "q":
                print("Program Sonlandırıldı.")
                break
            elif sayı == "d":
                print(işlemler)
                girdi = input("\nLütfen İşleminizi Giriniz: ")
            else:
                print("\nLütfen Sadece Sayı Giriniz.\n")

        # girilen sayıya kadar armstrong kontrolü
        if girdi == "3":
            sayı = input(
                "Şu anki İşlemi değiştirmek için d'ye basın. \nGirdiğiniz Sayıya Kadar Armstrong mu? Öğrenmek İçin: "
                "\n\nSayıyı Girin: ")
            if sayı.isdigit():
                arms_list = []
                for i in range(int(sayı)):
                    if armstrong(i):
                        arms_list.append(i)
                print("Girdiğiniz Sayıya Kadar Armstrong Listesi: {}\n".format(str(arms_list)[1:-1]))
            elif sayı == "q":
                print("Program Sonlandırıldı.")
                break
            elif sayı == "d":
                print(işlemler)
                girdi = input("\nLütfen İşleminizi Giriniz: ")
            else:
                print("\nLütfen Sadece Sayı Giriniz.\n")

        # asal kontrol
        if girdi == "4":
            sayı = input(
                "Şu anki İşlemi değiştirmek için d'ye basın. \nGirdiğiniz Sayıya Asal mı? Öğrenmek İçin: "
                "\n\nSayıyı Girin: ")
            if sayı.isdigit():
                if check(int(sayı)):
                    print("\n{} Asal Bir Sayıdır.\n".format(sayı))
                else:
                    print("\n{} Asal Bir Sayı Değildir.\n".format(sayı))
            elif sayı == "d":
                print(işlemler)
                girdi = input("\nLütfen İşleminizi Giriniz: ")
            elif sayı == "q":
                print("Program Sonlandırıldı.")
                break
            else:
                print("\nLütfen Sadece Sayı Giriniz.\n")

        # girilen sayıya kadar olan asallar
        if girdi == "5":
            sayı = input(
                "Şu anki İşlemi değiştirmek için d'ye basın. \nGirdiğiniz Sayıya Kadar Asal Olan Sayılar"
                " Öğrenmek İçin: \n\nSayıyı Girin: ")
            if sayı.isdigit():
                asallar = []
                for i in range(2, int(sayı)):
                    if check(i):
                        asallar.append(i)
                print("Girdiğiniz sayıya kadar olan asallar: \n\n> {}\n".format(str(asallar)[1:-1]))
            elif sayı == "d":
                print(işlemler)
                girdi = input("\nLütfen İşleminizi Giriniz: ")
            elif sayı == "q":
                print("Program Sonlandırıldı.")
                break
            else:
                print("\nLütfen Sadece Sayı Giriniz.\n")

        # tam bölenlerini bulma
        if girdi == "6":
            sayı = input(
                "Şu anki İşlemi değiştirmek için d'ye basın. \nGirdiğiniz Sayıyın Tam Bölenleri"
                " Öğrenmek İçin: \n\nSayıyı Girin: ")
            if sayı.isdigit():
                if divide(int(sayı)):
                    print("\n{} sayısının Tam Bölenleri: \n> {}\n".format(sayı, str(divide(int(sayı)))[1:-1]))
                elif sayı == "0":
                    print("Sıfırın Tam Böleni Yoktur.")
            elif sayı == "d":
                print(işlemler)
                girdi = input("\nLütfen İşleminizi Giriniz: ")
            elif sayı == "q":
                print("Program Sonlandırıldı.")
                break
            else:
                print("\nLütfen Sadece Sayı Giriniz.\n")

        # fibonacci serisi
        if girdi == "7":
            sayı = input(
                "Şu anki İşlemi değiştirmek için d'ye basın. \nFibonacci serisini"
                " Öğrenmek İçin: \n\nKaç Birim Uzunlukta Olsun: ")
            if sayı.isdigit():
                print("İlk {} Fibonacci Serisi:\n\n> {}\n".format(sayı, str(fibonacci(int(sayı)))[1:-1]))
            elif sayı == "d":
                print(işlemler)
                girdi = input("\nLütfen İşleminizi Giriniz: ")
            elif sayı == "q":
                print("Program Sonlandırıldı.")
                break
            else:
                print("\nLütfen Sadece Sayı Giriniz.\n")

        # Faktoriyal bulma
        if girdi == "8":
            sayı = input(
                "Şu anki İşlemi değiştirmek için d'ye basın. \nGirdiğiniz Sayının Faktoriyelini Bulma"
                " Öğrenmek İçin: \n\nSayıyı Girin: ")
            if sayı.isdigit():
                print("\n> {} sayısının faktoriyeli {}\n".format(sayı, factorial(int(sayı))))

            elif sayı == "d":
                print(işlemler)
                girdi = input("\nLütfen İşleminizi Giriniz: ")
            elif sayı == "q":
                print("Program Sonlandırıldı.")
                break
            else:
                print("\nLütfen Sadece Sayı Giriniz.\n")