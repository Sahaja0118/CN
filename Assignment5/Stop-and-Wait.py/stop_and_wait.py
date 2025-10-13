import random
import time

TOTAL_FRAMES = 5
LOSS_PROBABILITY = 0.3  
TIMEOUT = 2  

def send_frame(frame_no):
    print(f"Sending Frame {frame_no}")
    if random.random() < LOSS_PROBABILITY:
        print(f"Frame {frame_no} lost, retransmitting...")
        return False
    else:
        time.sleep(0.5)
        print(f"ACK {frame_no} received")
        return True

def stop_and_wait():
    frame_no = 0
    while frame_no < TOTAL_FRAMES:
        success = send_frame(frame_no)
        if success:
            frame_no += 1
        else:
            time.sleep(TIMEOUT)  

if __name__ == "__main__":
    print("---- Stop and Wait ARQ Simulation ----")
    stop_and_wait()
