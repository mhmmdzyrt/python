import random

print("""
Kırılması için aylar hatta yıllar geçmesi gereken şifreler oluşturmaya hazır mısınız? 
O halde başlayalım! Gelsin zorlu şifreler.
Unutmayın şifreniz ne kadar uzun ve karmaşıksa o kadar güvendesiniz demektir.
Oluşturulan şifrelerden dilediğinizi seçebilirsiniz. 
Ya da uç uca ekleyip daha da zorlu şifreler oluşturabilirsiniz.
Programdan çıkmaz için "q"'ya basmanız yeterli.
""")
entry = input('Kaç Şifre Oluşturulsun: ')

password = ""

while True:
    if entry.isdigit():
        choice = (input("\nÖnerilen uzunluk 8 - 12 hanedir.\n\nLütfen şifrenizin uzunluğunu giriniz: "))
        while True:
            if choice == "q":
                print("\nProgram sonlandırıldı.")
                break
            elif not choice.isdigit():
                print("\nLütfen sadece harf ya da sayı giriniz")
                choice = (input("\nÖnerilen uzunluk 8 ile 20 hanedir.\n\nLütfen şifrenizin uzunluğunu giriniz: "))
            elif int(choice) < 8:
                print("\nGüçlü bir şifre en az 8 haneden oluşmalıdır.\n")
                choice = (input("Hadi tekrar deneyelim!\n\nLütfen şifrenizin uzunluğunu giriniz: "))
            elif int(choice) >= 8:
                char = "abcdefghıijklmnoöprsştuüvyzABCDEFGĞHIİJKLMNOÖPRSŞTUÜVY:.Zé!'^@\"+%&/()=?_/*-+[]}{$#>£<€,;~"
                entry_1 = int(entry)
                for i in range(1, int(entry) + 1):
                    for j in range(int(choice)):
                        password += random.choice(char)
                        if len(password) == int(choice):
                            print('\n{}. Şifre: {}'.format(i, password))
                            password = ''
                break
        break
    elif entry == 'q':
        print("\nProgram sonlandırıldı.")
        break
    else:
        print('\nLütfen Sadece Sayı Giriniz!\n')
        entry = input('Kaç Şifre Oluşturulsun: ')