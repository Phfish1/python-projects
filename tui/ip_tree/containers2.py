from sortedcontainers import SortedKeyList, SortedList
from ipaddress import ip_network
from dataclasses import dataclass
import json
import re

@dataclass
class IPAttribute:
    comment: str = None

def main():

    sl = SortedKeyList(
            key=lambda node: (
                node.netmask
            )
    )

    
    with open("data/networks.json", "r") as file:
        net_json = json.load(file)
    
    for network in net_json:
        #try:
        #    attributes = IPAttribute(
        #                comment=network["comment"]
        #    )
        #except KeyError:
        #    attributes = IPAttribute(
        #            comment=None
        #    )

        sl.add(ip_network(network["network"]))

    #idx = sd.bisect_right("192.168.0.0")
    #print(sd.items()[idx])
    for item in sl:
        print(item)


    ### Queries the closest matching IP address to the users input
    while 1:
        user_ip = input("\nIP: ")
        
        u_octets = re.split(r"\.(?=.)", user_ip)
        if "." in u_octets[-1]:
            user_ip = user_ip[:-1]
        
        for i in range(0, 4 - len(u_octets)):
            user_ip += ".0"
      

        try:
            addr = ip_network(user_ip)
        except AddressValueError:
            print("Bad IP addr")
            continue


        idx = sl.bisect_left(addr)
        print(idx)

        for i in range(0,30):
            closest_match = sl[idx + i]
            print(f"{closest_match}") 




    return 0




if __name__ == "__main__":
    main()
