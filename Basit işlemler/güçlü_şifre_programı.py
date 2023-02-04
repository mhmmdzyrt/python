import random
print("""
Kırılması için aylar hatta yıllar geçmesi gereken şifreler oluşturmaya hazır mısınız? 
O halde başlayalım! Gelsin zorlu şifreler.
Unutmayın şifreniz ne kadar uzun ve karmaşıksa o kadar güvendesiniz demektir.
Oluşturulan 5 şifreden dilediğinizi seçebilirsiniz. 
Ya da uç uca ekleyip daha da zorlu şifreler oluşturabilirsiniz.
Programdan çıkmaz için "q"'ya basmanız yeterli.
""")
giriş = (input("Önerilen uzunluk 8 - 12 hanedir.\nLütfen şifrenizin uzunluğunu giriniz: "))
şifre1 = ""
şifre2 = ""
şifre3 = ""
şifre4 = ""
şifre5 = ""

while True:
    if giriş == "q":
        print("Program sonlandırıldı.")
        break
    if not giriş.isdigit():
        print("Lütfen sadece harf ya da sayı giriniz")
        giriş = (input("Önerilen uzunluk 8 ila 20 hanedir.\nLütfen şifrenizin uzunluğunu giriniz: "))
    elif int(giriş) < 8:
        print("\nGüçlü bir şifre en az 8 haneden oluşmalıdır.")
        giriş = (input("Hadi tekrar deneyelim!\nLütfen şifrenizin uzunluğunu giriniz: "))
    else:
        seçim = "abcdefghıijklmnoöprsştuüvyzABCDEFGĞHIİJKLMNOÖPRSŞTUÜVY:.Zé!'^@\"+%&/()=?_/*-+[]}{$#>£<€,;~"
        giriş = int(giriş)
        for i in range(giriş):
            şifre1 += random.choice(seçim)
            şifre2 += random.choice(seçim)
            şifre3 += random.choice(seçim)
            şifre4 += random.choice(seçim)
            şifre5 += random.choice(seçim)
        if len(şifre1) == giriş:
            print("Önerilen şifreler:\n\n1.Şifre: {}\n2.Şifre: {}\n3.Şifre: {}\n4.Şifre. {}\n5.Şifre: {}".format(şifre1, şifre2, şifre3, şifre4,şifre5))
            break
