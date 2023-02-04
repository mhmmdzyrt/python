def asal(sayı):
    if sayı == 1:
        return False
    if sayı == 2:
        return True
    for i in range(2,int(sayı**0.5)+1):
        if sayı % i ==0:
            return False
    return True

print("Çıkmak için q'ya basın.")
sayı = input("Sayı:")
while True:
    if sayı == "q":
        print("Program sonlandırılıyor.")
        break
    liste = ["1","2","3","4","5","6","7","8","9","0"]
    x = ""
    for i in sayı:
        if i in liste:
            x += i
    if x == sayı:
        if asal(int(sayı)):
            print(sayı,"asaldır.")
            sayı = input("Sayı:")
        else:
            print(sayı,"asal değildir.")
            sayı = input("Sayı:")
    else:
        print("Sadece sayı giriniz")
        sayı = input("Sayı:")