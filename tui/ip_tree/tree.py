import pytricia
from ipaddress import ip_network, IPv4Network, IPv4Address, AddressValueError
import json
from query import closest_ip

class Attributes:
    def __init__(self, location_id: string, vrf: string, vlan: string) -> None:
        self.location_id = location_id
        self.vrf = vrf
        self.vlan = vlan


a1 = Attributes("100", "BSR", "2")
a2 = Attributes("1392", "OBF", "999")

def main() -> None:
    pyt = pytricia.PyTricia()

    # The IP address being the Key, and Attributes the Value
    #pyt["172.0.0.0/8"] = a1
    #pyt["10.1.0.0/16"] = a2
    #pyt["10.1.1.0/24"] = a1
    #pyt["172.16.0.0/16"] = a1
    #pyt["10.0.0.0/8"] = a1
    #pyt["10.4.1.0/22"] = a1

    with open("data/networks.json", "r") as file:
        net_file = json.load(file)


    for network in net_file:
        try:
            pyt[network["network"]] = str(network["comment"])
        except KeyError:
            pyt[network["network"]] = "No comment"


    # This places our IP addresses in a Tree like structure
    #   NOT an hiearchical tree...
    #       All prefixes have ONLY one parent
    #       BUT, children of f.eg 10.0.0.0/8 are ALL addresses under that range,
    #           Not only direct children. (meaning also 10.1.1.0/24)...
    #
    #   This then requires special logic

    # !!! The pytrica tree IS ordered!
    #   Ordering by lowest ip address first.
    #   meaning first 10.0.0.0/8, then 10.1.0.0/16 etc....

    
    for ip in pyt:
        print(f"{ip} : {pyt.get(ip)}")#: [")

        # Accesses Key at current IP, treats it like a dict, then retrieves its Items(Key/Value)
        #for _, info in pyt.get(ip).__dict__.items():
        #    print(f"\t{info}")
        #print("]")
   
    
    # 00001010 . 00000000 . 00000000 . 00000000
    # Most unspesific address:
    # 11111110 . 00000000 . 00000000 . 00000000
    # /7
    #
    print(pyt.get_key(ip_network("10.0.0.0/24")))
    #closest_ip(pyt)
    #print(pyt.children("10.0.0.0/8"))





if __name__ == "__main__":
    main()

