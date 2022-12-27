from config import pg_user, pg_host, pg_port, pg_db_name, pg_password, mk_ip, mk_port, mk_user, mk_psw
from MikAPI import APImikrotik_v1
from mytools import Generate_PWD, get_new_ip4vpn

client_vpn_name = 'cl_test_222'
client_vpn_pwd = Generate_PWD(1,10)
cert_vpn_name = "cl_test_222"

inputcomand =""
command_to_mik ="ppp secret print"
print(command_to_mik)
connect = APImikrotik_v1(mk_ip, mk_port, mk_user, mk_psw, inputcomand, command_to_mik)

exit()
#client_ip = get_new_ip4vpn(1, getLog)
#print(client_ip)

#command_to_mik = 'certificate/add name={} common-name={} key-usage=tls-client key-size=4096 days-valid=3650'.format(cert_name,cert_name)

#command_to_mik ="/log print"





#####################################################################################
### Stop mik import

#print (inputcomand)


# lines = 0
# file = open('BackUp-Config-Mikrotik-Netmiko.txt')
# for line in file:
#     lines += 1
# print("Строк: ", line)