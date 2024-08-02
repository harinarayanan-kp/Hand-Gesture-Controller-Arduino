import cv2
import serial
from cvzone.HandTrackingModule import HandDetector

# Initialize serial connection with Arduino
com_port = 'COM6'  # Adjust COM port accordingly
baud_rate = 9600
ser = serial.Serial(com_port, baud_rate)

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)
video = cv2.VideoCapture(0)

# Variable to store the previous finger count
prev_finger_count = None

def send_command(finger_counts):
    command = ''.join(map(str, finger_counts)) + '\n'
    ser.write(command.encode())

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)
    
    if hands:
        lm_list = hands[0]
        finger_counts = detector.fingersUp(lm_list)
        
        # Print command only when finger count changes
        if finger_counts != prev_finger_count:
            print("Finger count:", finger_counts)
            send_command(finger_counts)
            prev_finger_count = finger_counts

    cv2.imshow("frame", frame)
    k = cv2.waitKey(10)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()
