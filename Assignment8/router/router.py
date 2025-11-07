# router.py
from Assignment8.ip_utils.ip_utils import ip_to_binary, get_network_prefix

class Router:
    def __init__(self, routes):
        """
        Initialize the router with a list of routes.
        Each route: (CIDR_prefix, output_link)
        """
        self.forwarding_table = self._build_forwarding_table(routes)

    def _build_forwarding_table(self, routes):
        """
        Convert routes to internal binary form and sort by prefix length (descending).
        """
        table = []
        for cidr, link in routes:
            binary_prefix = get_network_prefix(cidr)
            prefix_length = len(binary_prefix)
            table.append((binary_prefix, prefix_length, link))
        
        # Sort by prefix length (longest first)
        table.sort(key=lambda x: x[1], reverse=True)
        return table

    def route_packet(self, dest_ip: str) -> str:
        """
        Determine which link to send the packet to using Longest Prefix Match.
        """
        binary_ip = ip_to_binary(dest_ip)
        for prefix, _, link in self.forwarding_table:
            if binary_ip.startswith(prefix):
                return link
        return "Default Gateway"


# ---------- USER INPUT SECTION ----------
if __name__ == "__main__":
    print("---- Router Simulation ----")

    n = int(input("Enter number of routes: "))
    routes = []

    print("Enter each route in the form: CIDR  LinkName")
    print("Example: 223.1.1.0/24 Link0")
    
    for i in range(n):
        entry = input(f"Route {i+1}: ").strip().split()
        if len(entry) != 2:
            print("❌ Invalid format! Please use CIDR and LinkName separated by space.")
            exit()
        cidr, link = entry
        routes.append((cidr, link))
    
    router = Router(routes)

    while True:
        dest_ip = input("\nEnter destination IP (or 'exit' to quit): ").strip()
        if dest_ip.lower() == "exit":
            print("Exiting router simulation...")
            break
        result = router.route_packet(dest_ip)
        print(f"Packet sent to: {result}")
