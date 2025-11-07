# scheduler.py

from dataclasses import dataclass

@dataclass
class Packet:
    source_ip: str
    dest_ip: str
    payload: str
    priority: int   # 0 = High, 1 = Medium, 2 = Low


def fifo_scheduler(packet_list: list) -> list:
    """
    First-Come, First-Served scheduling.
    Packets are sent in the order they arrived.
    """
    # Simply return them in the same order
    return packet_list


def priority_scheduler(packet_list: list) -> list:
    """
    Priority-based scheduling.
    Lower priority number = higher priority.
    """
    # Sort based on packet.priority
    return sorted(packet_list, key=lambda pkt: pkt.priority)


# ---------- USER INPUT TEST ----------
if __name__ == "__main__":
    print("---- Output Port Scheduler ----")

    n = int(input("Enter number of packets: "))
    packets = []

    print("\nEnter packets in the form:")
    print("SourceIP  DestIP  Payload  Priority(0=High,1=Med,2=Low)")
    for i in range(n):
        src, dest, payload, pr = input(f"Packet {i+1}: ").split()
        packets.append(Packet(src, dest, payload, int(pr)))

    print("\n--- FIFO Order ---")
    fifo_order = fifo_scheduler(packets)
    for p in fifo_order:
        print(p.payload, end="  ")

    print("\n\n--- Priority Order ---")
    priority_order = priority_scheduler(packets)
    for p in priority_order:
        print(p.payload, end="  ")

    print("\n")
