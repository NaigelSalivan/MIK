from config import pg_user, pg_host, pg_port, pg_db_name, pg_password, mk_ip, mk_port, mk_user, mk_psw
from MikAPI import APImikrotik_v1

cert_name = "test"

command_to_mik = 'certificate/add name=' + cert_name + ' common-name=' + cert_name + ' key-usage=tls-client key-size=4096 days-valid=3650;'\
                 + 'certificate/add name=test2 common-name=test2 key-usage=tls-client key-size=4096 days-valid=3650'

#command_to_mik = 'certificate/add name={} common-name={} key-usage=tls-client key-size=4096 days-valid=3650'.format(name,name)

print (command_to_mik)

print (command_to_mik)
inputcomand ="/ip firewall address-list add address=69.23.209.0/24 list=\"blok IP\""
# outputcomand ="/log print where message~\"pptp\"" \"logged\"
# certificate/add name=test common-name=test key-usage=tls-client key-size=4096 days-valid=3650
#    certificate/add name=test common-name=test key-usage=tls-client key-size=4096 days-valid=3650
outputcomand = command_to_mik #"/ip/address/print"
command_to_mik2 = 'certificate/sign name=' + cert_name + ' ca=newCA'
outputcomand2 = command_to_mik2

# outputcomand ="/log print where topics~\"error\""
# outputcomand =""
connect = APImikrotik_v1(mk_ip, mk_port, mk_user, mk_psw, inputcomand, outputcomand)
# lines = 0
# file = open('BackUp-Config-Mikrotik-Netmiko.txt')
# for line in file:
#     lines += 1
# print("Строк: ", line)