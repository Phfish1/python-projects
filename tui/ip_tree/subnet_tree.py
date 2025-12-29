import radix
import json
from ipaddress import ip_network, IPv4Address
from sortedcontainers import SortedKeyList

def get_lowest_netmask(ip_address: IPv4Address) -> int:
    ip_byte = int.from_bytes(ip_address.packed, byteorder="big")

    bitshift_c = 0
    while not (ip_byte & 1):
        ip_byte = ip_byte >> 1

        bitshift_c += 1
    
    lowest_netmask = 32 - bitshift_c

    return lowest_netmask


    #
    # search_tree(ip_tree: radix.Radix, ip_input: IPv4Address) -> List:
    #   ...
    #   return rnodes
    #
    # This code needs to search containers UNTIL,
    #   There is only one containers left!
    #   THEN search networks contained under the container selected...
    #       This is NOT done within this function
    #
    ### : START :
def search_rtree(rtree: radix.Radix, ip_input: IPv4Address) -> List:
    lowest_netmask = get_lowest_netmask(ip_input)

    rnode = None
    count = 1
    while rnode == None and count <= 30:
        rnode = rtree.search_best(f"{ip_input}/{lowest_netmask}")

        # Exception if IP address is exact on first loop
        exact_rnode = rtree.search_exact(f"{ip_input}/{lowest_netmask}")
        if exact_rnode != None:
            rnode = exact_rnode
            break

        # Loop variables
        lowest_netmask += 1
        count += 1

        # Exception if IP address is exact on later loops
        exact_rnode = rtree.search_exact(f"{ip_input}/{lowest_netmask}")
        if exact_rnode != None:
            rnode = exact_rnode

    if rnode != None:
        print("Radix search")
        print(rnode.prefix)
        print()
        rnodes = rtree.search_covered(rnode.prefix)
    else:
        print("SortedList search")
        print()
        cont_search = cont_ls.bisect_left(ip_network(ip_input)) 
        rnodes = rtree.search_covered(cont_ls[cont_search].with_prefixlen)

    return rnodes
    ### : END : 


def main():
    containers = radix.Radix()
    networks = radix.Radix()

    with open("data/networkcontainers.json", "r") as file:
        cont_file = json.load(file)

    with open("data/networks.json", "r") as file:
        net_file = json.load(file)

    for cont in cont_file:
        containers.add(cont["network"])

    for net in net_file:
        networks.add(net["network"])


    #
    # Setting up SortedLists
    #

    cont_ls = SortedKeyList(
            key=lambda node: (
                node.network_address
            )
    )

    for cont in containers:
        cont_ls.add(ip_network(cont.prefix))

    #
    # Other code: 
    #

    #ip_input = IPv4Address("192.168.64.0")
    ip_input = IPv4Address("10.1.16.0")
    


    rnodes = search_rtree(containers, ip_input)
  
    # THIS SEARCHES NETWORKs, UNDER the container !
    if len(rnodes) == 1:
        rnodes = networks.search_covered(rnodes[0].prefix)

    # IF size of rnodes == 1
    #   Do a networks.search_covered(rnodes[0].prefix)

    #
    # Gets all IP Networks under the most spesefic container
    #
    #rnodes = networks.search_covered(rnode.prefix)

    # Create SortedList for searching?
    sl = SortedKeyList(
            key=lambda node: (
                node.network_address
            )
    )

    for node in rnodes:
        sl.add(ip_network(node.prefix))
   
    idx = sl.bisect_left(ip_network(ip_input))

    for i in range(idx, sl.__len__()):
        print(sl[i])
    
    #for covered_net in rnodes:
    #    print(covered_net.prefix)
    


    #print(lowest_netmask)
    #print(rnode.prefix)
    #for net in rtree:
    #    print(net.prefix)
    #rnodes = rtree.search_covered("10.0.0.0/0")
    #for covered_net in rnodes:
    #    print(covered_net.prefix)



if __name__ == "__main__":
    main()
