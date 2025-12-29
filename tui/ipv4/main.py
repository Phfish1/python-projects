from ipaddress import ip_network, IPv4Address

def main():
    a1 = ip_network("10.1.0.0/24")
    print(a1.make_netmask)


main()
