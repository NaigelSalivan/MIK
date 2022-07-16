from config import pg_user, pg_host, pg_port, pg_db_name, pg_password, mk_ip, mk_port, mk_user, mk_psw
from MikAPI import APImikrotik_v1

# inputcomand ="/ip firewall address-list add address=69.23.209.0/24 list=\"blok IP\""
inputcomand =""
outputcomand ="/log print where message~\"pptp\""
# outputcomand =""
connect = APImikrotik_v1(mk_ip, mk_port, mk_user, mk_psw, inputcomand, outputcomand)
# lines = 0
# file = open('BackUp-Config-Mikrotik-Netmiko.txt')
# for line in file:
#     lines += 1
# print("Строк: ", line)