import pytricia
import re
from ipaddress import ip_network, IPv4Network, IPv4Address, AddressValueError

class Attributes:
    def __init__(self, location_id: string, vrf: string, vlan: string) -> None:
        self.location_id = location_id
        self.vrf = vrf
        self.vlan = vlan


a1 = Attributes("100", "BSR", "2")
a2 = Attributes("1392", "OBF", "999")

pyt = pytricia.PyTricia()

# The IP address being the Key, and Attributes the Value
pyt["10.0.0.0/8"] = a1
pyt["10.1.0.0/16"] = a2
pyt["10.1.1.0/24"] = a1
pyt["10.4.1.0/22"] = a1

def closest_ip(pyt: PyTricia) -> None:


    # This places our IP addresses in a Tree like structure
    #   NOT an hiearchical tree...
    #       All prefixes have ONLY one parent
    #       BUT, children of f.eg 10.0.0.0/8 are ALL addresses under that range,
    #           Not only direct children. (meaning also 10.1.1.0/24)...
    #
    #   This then requires special logic

    # The pytricia tree is great for closet lookups!
    #   But it need to take in an entire ip/prefix to do its lookup 


    ### Queries the closest matching IP address to the users input
    while 1:
        user_ip = input("IP: ")
        
        u_octets = re.split(r"\.(?=.)", user_ip)
        if "." in u_octets[-1]:
            user_ip = user_ip[:-1]
        
        for i in range(0, 4 - len(u_octets)):
            user_ip += ".0"
      

        try:
            addr = IPv4Address(user_ip)
        except AddressValueError:
            print("Bad IP addr")
            continue


        closest_match = pyt.get_key(f"{addr}") 
        if closest_match == None:
            print("No IP found")
            continue
        
        print(addr)
        print(closest_match, pyt.get(closest_match)) # Prints IP + 'attribute'





if __name__ == "__main__":
    closest_ip(pyt)
