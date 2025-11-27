# AS-level topology (undirected graph)
topology = {
    'AS1': ['AS2', 'AS3'],
    'AS2': ['AS1', 'AS3', 'AS4'],
    'AS3': ['AS1', 'AS2', 'AS5'],
    'AS4': ['AS2', 'AS5'],
    'AS5': ['AS3', 'AS4']
}

def initialize_bgp_tables(topology):
    tables = {}
    for asn in topology:
        # Format: destination -> path list
        tables[asn] = {asn: [asn]}
    return tables

def bgp_update(topology, tables):
    updated = False
    new_tables = {asn: tables[asn].copy() for asn in topology}

    for asn in topology:
        for neighbor in topology[asn]:
            for dest, path in tables[asn].items():
                # Loop prevention: ignore if neighbor already in path
                if neighbor in path:
                    continue

                new_path = [neighbor] + path

                # Add or update if shorter AS path found
                if (dest not in new_tables[neighbor] or
                    len(new_path) < len(new_tables[neighbor][dest])):
                    new_tables[neighbor][dest] = new_path
                    updated = True

    return new_tables, updated

def simulate_bgp(topology):
    tables = initialize_bgp_tables(topology)
    converged = False
    rounds = 0

    print("Initial Routing Tables:")
    print_bgp_tables(tables)

    while not converged:
        rounds += 1
        tables, updated = bgp_update(topology, tables)
        print(f"\nAfter round {rounds}:")
        print_bgp_tables(tables)
        if not updated:
            converged = True

    print(f"\n✅ BGP converged after {rounds} update rounds.")
    return tables

def print_bgp_tables(tables):
    for asn, routes in tables.items():
        print(f"\n{asn} Routing Table:")
        print("Destination | AS Path")
        print("----------------------")
        for dest, path in routes.items():
            print(f"    {dest}      | {' → '.join(path)}")

if __name__ == "__main__":
    final_tables = simulate_bgp(topology)
