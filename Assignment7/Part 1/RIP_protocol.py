# Network topology (example)
# network = {
#     'A': {'B': 1, 'C': 1},
#     'B': {'A': 1, 'C': 1, 'D': 1},
#     'C': {'A': 1, 'B': 1, 'D': 1},
#     'D': {'B': 1, 'C': 1}
# }

network = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 3},
    'C': {'A': 5, 'B': 1, 'D': 2, 'E': 3},
    'D': {'B': 3, 'C': 2, 'E': 1},
    'E': {'C': 3, 'D': 1}
}

def initialize_distance_vectors(network):
    distance_vectors = {}
    next_hops = {}

    for router in network:
        distance_vectors[router] = {dest: float('inf') for dest in network}
        next_hops[router] = {dest: None for dest in network}
        distance_vectors[router][router] = 0
        next_hops[router][router] = router
        for neighbor, cost in network[router].items():
            distance_vectors[router][neighbor] = cost
            next_hops[router][neighbor] = neighbor
    return distance_vectors, next_hops

def bellman_ford_update(network, distance_vectors, next_hops):
    updated = False
    new_vectors = {r: distance_vectors[r].copy() for r in network}
    new_hops = {r: next_hops[r].copy() for r in network}

    for router in network:
        for neighbor, cost in network[router].items():
            for dest in distance_vectors[neighbor]:
                new_dist = distance_vectors[neighbor][dest] + cost
                if new_dist < new_vectors[router][dest]:
                    new_vectors[router][dest] = new_dist
                    # The next hop is the neighbor (first hop toward dest)
                    new_hops[router][dest] = neighbor
                    updated = True
    return new_vectors, new_hops, updated

def simulate_rip(network):
    distance_vectors, next_hops = initialize_distance_vectors(network)
    converged = False
    rounds = 0

    print("Initial Routing Tables:\n")
    print_routing_tables(distance_vectors, next_hops)

    while not converged:
        rounds += 1
        distance_vectors, next_hops, updated = bellman_ford_update(network, distance_vectors, next_hops)
        print(f"\nAfter round {rounds}:")
        print_routing_tables(distance_vectors, next_hops)
        if not updated:
            converged = True

    print(f"\n✅ Converged after {rounds} update rounds.")
    return distance_vectors, next_hops

def print_routing_tables(distance_vectors, next_hops):
    for router, table in distance_vectors.items():
        print(f"Router {router}:")
        for dest, dist in sorted(table.items()):
            nh = next_hops[router][dest]
            print(f"  {dest}: {dist if dist != float('inf') else '∞'} hops via {nh if nh else '-'}")
        print()

if __name__ == "__main__":
    final_vectors, final_next_hops = simulate_rip(network)
