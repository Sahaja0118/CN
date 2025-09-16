import socket
import cv2
import numpy as np
import time

HOST = '127.0.0.1'         
PORT=5001              
CHUNK_SIZE=4096        

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

VIDEO_SOURCE = "Assignment4/sample.mp4"  
cap = cv2.VideoCapture(VIDEO_SOURCE)

if not cap.isOpened():
    print("Error: Unable to open video file")
    exit()

FPS=cap.get(cv2.CAP_PROP_FPS)
frame_interval=1.0/FPS if FPS else 0.04  

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    
    frame=cv2.resize(frame, (640, 480))

    encoded,buffer=cv2.imencode('.jpg', frame)
    byte_data=buffer.tobytes()

    for i in range(0, len(byte_data), CHUNK_SIZE):
        chunk=byte_data[i:i+CHUNK_SIZE]
        marker=1 if i + CHUNK_SIZE>=len(byte_data) else 0

        data=marker.to_bytes(1,'big')+chunk
        sock.sendto(data,(HOST, PORT))

    time.sleep(frame_interval)

cap.release()
sock.close()
print("Video streaming complete.")
