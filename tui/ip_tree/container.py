from sortedcontainers import SortedList
from ipaddress import ip_network
import json
import re
from dataclasses import dataclass, field


def main():
    @dataclass
    class IPNode:
        network: object
        comment: str = ""

    # Creates a SortedList that orders based on network prefix length
    sl = SortedList(
            key=lambda node: (
                int(node.network.network_address), 
                node.network.prefixlen
            )
    )

    with open("data/networks.json", "r") as file:
        net_json = json.load(file)

    ### Adds each Network as a IPNode to the SortedList
    for network in net_json:
        try:
            node = IPNode(
                network=ip_network(network["network"]),
                comment=network["comment"]
            )
        except KeyError:
            node = IPNode(
                    network=ip_network(network["network"]),
                    comment=None
            )

        sl.add(node)
   
    #idx = sl.bisect_left(IPNode(ip_network("192.0.0.0")))
    #print(f"{sl[idx].network} : {sl[idx].comment}") 


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


        idx = sl.bisect_left(IPNode(addr))
       
        for i in range(0,10):
            closest_match = sl[idx + i]
            print(f"{closest_match.network} : {closest_match.comment}") 






if __name__ == "__main__":
    main()


