import tld
import socket
import os
import subprocess
import time


def get_top_level_domain(url):
    try:
        name = tld.get_tld(url)
        return name
    except tld.exceptions.TldBadUrl:

        return -1


def get_IP_Address(url):
        return socket.gethostbyname_ex(url)


def web_url_sections():
    url = input("Enter the web server url: ")
    domain_name = get_top_level_domain(url)

    if get_top_level_domain(url) == -1:
        print("The url is not in the correct format remember https://......")
        print("*******************************************************")
        print("*******************************************************")
        return url
    print("******************************************************")
    print("These are the associations(raw) for that Domain name :")
    for i in range(len(get_IP_Address(domain_name))):
        list1 = get_IP_Address(domain_name)
        if (len(list1[i])) >= 1 and (list1[i] != domain_name):
            print(str(list1[i])[1:-1])
    print("******************************************************")
    print("\n")
    if os.system("ping " + domain_name) == 0:
        print("System is up")
    else:
        print("System is not responding to ICMP requests")


i = 'yes'
ping_count = 0
while i == 'yes':
    print("******************************************")
    print("Welcome to this Basic scanner")
    if input("Local or Remote?") == 'Local':
        # Check for hosts alive on the network
        IP = input("Enter the network ID eg:(192.168.0.xxx): ")
        starting_time = time.clock()
        for m in range(255):
            exitcode, output = subprocess.getstatusoutput("ping " + str(IP)+ str(m)+" -w 1 -n 1")
            if exitcode == 0:
                print("System " + IP + str(m) + " is UP !")
                ping_count += 1
        print("Currently there are "+str(ping_count)+" hosts alive")
        print("Program took "+str(round(time.clock() - starting_time,1))+" Seconds to find hosts alive")
    else:
        # incomplete
        web_url_sections()

