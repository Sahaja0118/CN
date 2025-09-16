import socket
import cv2
import numpy as np

HOST='0.0.0.0'   
PORT=5001        
CHUNK_SIZE=4096

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print("Client listening for video stream...")
while True:
    frame_data = b''
    while True:
        packet, _ = sock.recvfrom(CHUNK_SIZE + 1)
        
        if packet == b'END':
            print("End of stream received.")
            sock.close()
            cv2.destroyAllWindows()
            exit(0)

        marker = packet[0]
        chunk = packet[1:]
        frame_data += chunk
        if marker == 1:
            break

    np_data = np.frombuffer(frame_data, np.uint8)
    frame = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
    if frame is not None:
        cv2.imshow('UDP Video Stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
sock.close()
