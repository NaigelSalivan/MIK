import netmiko
from netmiko import ConnectHandler
class APImikrotik_v1:
    def __init__(self, mk_ip, mk_port, mk_user, mk_psw, inputcomand, outputcomand):
        self.mk_ip=mk_ip
        self.mk_port=mk_port
        self.mk_user=mk_user
        self.mk_psw=mk_psw
        self.inputcomand=inputcomand
        self.outputcomand=outputcomand

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
            # file = open("BackUp-Config-Mikrotik-Netmiko.txt", "w")
            getLog = output.split("\n")

            dOutput = []
            n=0

            for elemet in getLog:
                a = elemet.strip()

                aformated = a.split(" ", 2)
                if aformated[1] == 'pptp,ppp,info':
                    aformated[2] = aformated[2].split(":")
                    print(aformated)

                dOutput.append(aformated)
                # dOutput.append(a.split(" ", 2))

                # print(dOutput[n][1] + " : " + dOutput[n][2])

                if n != len(getLog):
                    n += 1
                else:
                    break

            # print(len(getLog))
            print(dOutput)

            # with open('BackUp-Config-Mikrotik-Netmiko.txt', 'w') as filehandle:
            #     for listitem in dOutput:
            #         filehandle.write('%s\n' % listitem)


            # file.write(OutputTxt)
            # file.close()
            # command = self.inputcomand




        sshCli.disconnect()