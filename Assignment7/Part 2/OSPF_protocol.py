# Example network graph (weighted edges)
network = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 3},
    'C': {'A': 5, 'B': 1, 'D': 2, 'E': 3},
    'D': {'B': 3, 'C': 2, 'E': 1},
    'E': {'C': 3, 'D': 1}
}

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

def simulate_lsa_exchange(network):
    # Each router builds its link-state database (the full graph)
    lsdb = {router: network.copy() for router in network}
    return lsdb

def build_routing_tables(lsdb):
    routing_tables = {}

    for router in lsdb:
        graph = lsdb[router]
        distances, previous = dijkstra(graph, router)

        routing_table = {}
        for dest in graph:
            if dest == router:
                continue

            # Backtrack to find next hop
            next_hop = dest
            while previous[next_hop] != router and previous[next_hop] is not None:
                next_hop = previous[next_hop]

            routing_table[dest] = {
                "Next Hop": next_hop if previous[dest] else "-",
                "Cost": distances[dest]
            }

        routing_tables[router] = routing_table

    return routing_tables

def print_routing_tables(routing_tables):
    for router, table in routing_tables.items():
        print(f"\nRouter {router} Routing Table:")
        print("Destination | Next Hop | Cost")
        print("-----------------------------")
        for dest, info in table.items():
            print(f"     {dest}       |    {info['Next Hop']}    |  {info['Cost']}")

if __name__ == "__main__":
    lsdb = simulate_lsa_exchange(network)
    routing_tables = build_routing_tables(lsdb)
    print_routing_tables(routing_tables)

