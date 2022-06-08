sifre = int(input("şifre giriniz:"))
x = 1
while sifre != 1234:
    print("şifre yanlış!")
    x +=1
    sifre = int(input("şifre giriniz:"))
    if x == 3:
        print("3 kez hatali giris yaptiniz.")
        break
if sifre == 1234:
    print("şifre doğru.")