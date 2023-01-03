import random
import re


def Generate_PWD(quantity, length):
    quantity_pwd = int(quantity)  # количество паролей
    length_pwd = int(length)  # длина пароля

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


def get_new_ip4vpn(quantity, output_console):
    quantity_ip = int(quantity)
    # command_to_mik = "ppp secret print"
    output_console = str(output_console).split("\n")
    ip_vpn_list = []
    # print(output_console)
    for elemet in output_console:
        curent_item_ip = elemet.strip()
        result = re.search(
            r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))', curent_item_ip)
        if result != None:
            # print(result.group(0))
            ip_vpn_list.append(result.group(0).split("."))
            ip_vpn_list[-1] = list(map(int, ip_vpn_list[-1]))
    ip_vpn_list.sort()

    last_ip = ip_vpn_list[-1]
    pozition_addr = last_ip
    new_ip_list = []
    i = 0
    while i < quantity_ip:
        pozition_addr[3] = int(pozition_addr[3]) + i
        print(pozition_addr)
        new_ip_list.append(pozition_addr[3])
        #new_ip_list = ".".join(map(str, pozition_addr))
        i+=1
        #print('===' + pozition_addr.__str__())
    # print(last_ip)
    #

    return new_ip_list

# print(Generate_PWD(1,10),)

#   создание пользователя
# ppp/secret/add name=test password=pwd service=ovpn profile=General_OVPN remote-address=
#
#   Получение списка пользователей по профилю
# ppp/secret/print where profile=General_OVPN

######################## Парсер лога
# if input_if == 1:
#     for elemet in getLog:
#         a = elemet.strip()
#
#         aformated = a.split(" ", 2)
#
#         if aformated[1] == 'pptp,ppp,info':
#             aformated[2] = aformated[2].strip().split(":")
#             # print(aformated)
#         if aformated[1] == 'system,info,account':
#             aformated[2] = aformated[2].strip().split(":")
#         print(aformated)
#         if 'error' in aformated[1]:
#             # textLog = ' '.join(map(str, aformated[2]))
#             textStringLog = "".join(aformated[2])
#
#             # print("Inter: " + textStringLog)
#             textStringLog = textStringLog.replace(' from', '')
#
#             textStringLog = textStringLog.replace(' user', '', 1)
#             textStringLog = textStringLog.replace(' via', '', 1)
#             textStringLog = textStringLog.replace(' for', '', 1)
#             textStringLog = textStringLog.replace('to romon network', 'romon_network', 1)
#             textStringLog = textStringLog.replace(' ', '_', 1)
#
#             # print("Exit: " + textStringLog)
#             aformated[2] = textStringLog.strip().split(" ")
#             # print("Data tools: " + textStringLog)
#             print(aformated)
#
#             dOutput.append(aformated)
#             # dOutput.append(a.split(" ", 2))
#
#             # print(dOutput[n][1] + " : " + dOutput[n][2])
#
#             if n != len(getLog):
#                 n += 1
#             else:
