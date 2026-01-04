import cv2
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video_cap = cv2.VideoCapture(0)

try:
    while True:
        ret, video_data = video_cap.read()
        if not ret:
            break
            
        frame_rgb = cv2.cvtColor(video_data, cv2.COLOR_BGR2RGB)
        
        faces = face_cap.detectMultiScale(
            frame_rgb,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)

        plt.figure(figsize=(10, 6))
        plt.imshow(frame_rgb)
        plt.axis('off')
        plt.show()
        
        clear_output(wait=True)

except KeyboardInterrupt:
    video_cap.release()
    print("Stream stopped")
    
video_cap.release()
