import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Şifre uzunluğunu giriniz"))

parola = ""
for i in range(uzunluk):
    parola +=  random.choice(karakterler)

print(parola)
