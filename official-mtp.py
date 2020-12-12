import os, requests
from time import sleep

def FileExist(path):
    try:
        open(path)
    except:
        return False
    else:
        return True

if FileExist(f"MTProxy/Makefile"):
    print("MTProxy Folder Found!")
else:
    os.system("apt update -y")
    os.system("apt install git curl build-essential libssl-dev zlib1g-dev -y")
    os.system("git clone https://github.com/TelegramMessenger/MTProxy")
    os.system("cd MTProxy && make && cd objs/bin && curl -s https://core.telegram.org/getProxySecret -o proxy-secret && curl -s https://core.telegram.org/getProxyConfig -o proxy-multi.conf")

port = input("Enter the port: ") or "88"
secret = input("Enter the secret: ") or "00000000000000000000000000000000"
tls = input("Enter the TLS: (Baraye Nasle 2 dd khali bzarid o Enter konid) ")
tag = input("Enter the sponser tag: ") or "ea58002650356009cf671c4ffd14b684"
cpu = input("Enter the number of Cpu core: ") or "2"



if tls == None:
    if FileExist(f"/etc/systemd/system/MTProxy.service"):
        os.remove("/etc/systemd/system/MTProxy.service")
    ff = open("/etc/systemd/system/MTProxy.service", "w")
    ff.write('''[Unit]
Description=MTProxy
After=network.target

[Service]
Type=simple
WorkingDirectory=/root/MTProxy/objs/bin
ExecStart=/root/MTProxy/objs/bin/mtproto-proxy -u nobody -p 7777 -H '''+str(port)+''' -S '''+str(secret)+''' -P '''+str(tag)+''' --aes-pwd proxy-secret proxy-multi.conf -M '''+str(cpu)+'''
Restart=on-failure

[Install]
WantedBy=multi-user.target''')
    ff.close()
    os.system("systemctl daemon-reload")
    sleep(2)
    os.system("systemctl restart MTProxy.service")
    os.system("systemctl enable MTProxy.service")
    ip = requests.get("https://api.ipify.org")
    print(f"https://t.me/proxy?server={ip}&port={port}&secret=dd{secret}")

else:
    if FileExist(f"/etc/systemd/system/MTProxy.service"):
        os.remove("/etc/systemd/system/MTProxy-TLS.service")
    ff = open("/etc/systemd/system/MTProxy-TLS.service", "w")
    ff.write('''[Unit]
Description=MTProxy-TLS
After=network.target

[Service]
Type=simple
WorkingDirectory=/root/MTProxy/objs/bin
ExecStart=/root/MTProxy/objs/bin/mtproto-proxy -u nobody -p 8888 -H '''+str(port)+''' -S '''+str(secret)+''' -P '''+str(tag)+''' --aes-pwd proxy-secret proxy-multi.conf -M '''+str(cpu)+''' -D '''+str(tls)+'''
Restart=on-failure

[Install]
WantedBy=multi-user.target''')
    ff.close()
    os.system("systemctl daemon-reload")
    sleep(2)
    os.system("systemctl restart MTProxy-TLS.service")
    os.system("systemctl enable MTProxy-TLS.service")
    get = requests.get("https://api.ipify.org")
    ip = get.text
    tlsdecode = (tls).encode("utf-8").hex()
    print(tlsdecode)
    print(f"https://t.me/proxy?server={ip}&port={port}&secret=ee{secret}{tlsdecode}")
