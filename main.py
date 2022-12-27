from config import pg_user, pg_host, pg_port, pg_db_name, pg_password, mk_ip, mk_port, mk_user, mk_psw
from MikAPI import APImikrotik_v1
from mytools import Generate_PWD

#pwd = Generate_PWD(1,10)
cert_name = "cl_test_222"

#command_to_mik = 'certificate/add name={} common-name={} key-usage=tls-client key-size=4096 days-valid=3650'.format(cert_name,cert_name)
command_to_mik ="ppp/secret/print where profile=General_OVPN"
#command_to_mik ="/log print"
inputcomand =""



print (command_to_mik)
outputcomand = command_to_mik


#####################################################################################
### Stop mik import
connect = APImikrotik_v1(mk_ip, mk_port, mk_user, mk_psw, inputcomand, outputcomand)
print (inputcomand)


# lines = 0
# file = open('BackUp-Config-Mikrotik-Netmiko.txt')
# for line in file:
#     lines += 1
# print("Строк: ", line)