# OpenCV module used to detect cats
import cv2
import cloudinary
import cloudinary.uploader
import vonage
from soundplayer import SoundPlayer
import time

# Config for uploading photos to Cloudinary
cloudinary.config(
    cloud_name = "dc3kwd5bv",
    api_key = "352432556567254",
    api_secret = "l10PA1N-OvZj49AKNwtTAZtQ1tk"
)

# Initialize Vonage client for sending SMS
client = vonage.Client(key="dd806ca0", secret="Hyst7R37Qm01mOTV")
sms = vonage.Sms(client)

# Function used to send SMS text messages through Vonage
def sendSMS(url):
    responseData = sms.send_message(
        {
            "from": "18778232501",
            "to": "12135191036",
            "text": "Cat detected! See the photo at: " + url,
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

# Data used to classify cat faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml') 

# Start video capture from picamera module
cap = cv2.VideoCapture(0) 

i = 0

while 1: 
  
    # Read frames from camera
    ret, img = cap.read()
    # Rotate frames 90 degrees counterclockwise due to orientation of picamera
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
  
    # Convert each frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # Detect faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

    if (len(faces) > 0):
        for (x, y, w, h) in faces: 
            # Draw rectangles around cat faces
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
        filename = 'image_' + str(i) + '.jpg'
        # Write image out to a jpg file
        cv2.imwrite(filename, img)
        upload = cloudinary.uploader.upload(filename)
        sendSMS(upload['url'])
        break

    # Display image in a window (when testing)
    # cv2.imshow('img', img) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
# Close the window
cap.release() 
  
# De-allocate any associated memory usage
cv2.destroyAllWindows()
