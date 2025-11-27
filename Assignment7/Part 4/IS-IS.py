# Example IS-IS network topology
network = {
    'R1': {'R2': 2, 'R3': 4},
    'R2': {'R1': 2, 'R3': 1, 'R4': 7},
    'R3': {'R1': 4, 'R2': 1, 'R4': 3, 'R5': 2},
    'R4': {'R2': 7, 'R3': 3, 'R5': 1},
    'R5': {'R3': 2, 'R4': 1}
}

def flood_link_state(network):
    # Each router learns the full network topology (LSDB synchronization)
    lsdb = {router: network.copy() for router in network}
    return lsdb

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
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                heapq.heappush(pq, (new_dist, neighbor))

    return distances, previous

def build_routing_tables(lsdb):
    routing_tables = {}

    for router in lsdb:
        graph = lsdb[router]
        distances, previous = dijkstra(graph, router)

        routing_table = {}
        for dest in graph:
            if dest == router:
                continue

            # Determine next hop by backtracking
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
    lsdb = flood_link_state(network)
    routing_tables = build_routing_tables(lsdb)
    print_routing_tables(routing_tables)
