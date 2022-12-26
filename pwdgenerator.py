import random

def Generate_PWD(quantity, length):
    quantity_pwd = int(quantity)     #количество паролей
    length_pwd = int(length)         #длина пароля

    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    pwd_list = []
    # number = int(number)
    # length = int(length)
    for n in range(quantity_pwd):
        password = ''
        for i in range(length_pwd):
            password += random.choice(chars)
        print('сгенерирован: ' + password)
        pwd_list.append(password)
    return pwd_list

print(Generate_PWD(1,10),)