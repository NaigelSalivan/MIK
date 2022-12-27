import netmiko
from netmiko import ConnectHandler

from mytools import get_new_ip4vpn

class APImikrotik_v1:
    def __init__(self, mk_ip, mk_port, mk_user, mk_psw, inputcomand, outputcomand):
        self.mk_ip = mk_ip
        self.mk_port = mk_port
        self.mk_user = mk_user
        self.mk_psw = mk_psw
        self.inputcomand = inputcomand
        self.outputcomand = outputcomand

        mikrotik_router_1 = {
            'device_type': 'mikrotik_routeros',
            'host': self.mk_ip,
            'port': self.mk_port,
            'username': self.mk_user,
            'password': self.mk_psw
        }

        sshCli = ConnectHandler(**mikrotik_router_1)
        if inputcomand.strip():
            input = sshCli.send_command(inputcomand)

        if outputcomand.strip():
            output = sshCli.send_command(outputcomand)
            users_vpn = get_new_ip4vpn(output)


            print(users_vpn)
        sshCli.disconnect()



