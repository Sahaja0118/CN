import matplotlib.pyplot as plt
import random

TOTAL_ROUNDS = 30
LOSS_PROBABILITY = 0.15
THRESHOLD = 8

def tcp_congestion_control():
    cwnd = 1
    threshold = THRESHOLD
    cwnd_values = []

    for round_no in range(1, TOTAL_ROUNDS + 1):
        cwnd_values.append(cwnd)
        print(f"Round {round_no}: cwnd = {cwnd}")

        if random.random() < LOSS_PROBABILITY:
            print(f"Packet loss detected! Threshold set to {max(1, cwnd // 2)}")
            threshold = max(1, cwnd // 2)
            cwnd = 1  
            continue

        if cwnd < threshold:
            cwnd *= 2  
        else:
            cwnd += 1  
            
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, TOTAL_ROUNDS + 1), cwnd_values, marker='o')
    plt.title("TCP Congestion Control Simulation")
    plt.xlabel("Transmission Rounds")
    plt.ylabel("Congestion Window (cwnd)")
    plt.grid(True)
    plt.savefig("cwnd_plot.png")
    plt.show()

if __name__ == "__main__":
    tcp_congestion_control()
