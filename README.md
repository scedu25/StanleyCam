# StanleyCam
This is my final project for CS498: Internet of Things.<br><br>
<img src=https://res.cloudinary.com/dc3kwd5bv/image/upload/v1621225434/qt6lzuh4kemfwbi2tdjx.jpg width=30%>

---

### Introduction
StanleyCam is a pet monitor built using a Raspberry Pi 4 with a camera module. Python and OpenCV are used for cat facial recognition to detect when my cat, Stanley, gets on the counter. When this happens, the following series of events is triggered:
- A loud vacuum noise (he hates our vacuum) is played through a nearby bluetooth speaker.
- A photo is taken of Stanley and uploaded to Cloudinary for storage.
- An SMS text message is sent to my phone along with the newly uploaded photo URL.

The motivation for this project came from my tabby cat Stanley, who must often be scolded for jumping on the counter. Stanley has an insatiable appetite. Although we have for the most part trained him to avoid the kitchen when we’re at home, we weren't sure how often he'd snoop around with no one there to catch him. So I decided to create a pet monitor that could alert us when we're away from home.

### Specifications
The hardware set up was rather straightforward. I installed Raspberry Pi OS on a Raspberry Pi 4 and connected the Raspberry Pi Camera Module. I bought a case for the Raspberry Pi so that it could be placed on its side. The camera's ribbon cable was looped around and taped to the front of the case. The Raspberry Pi was positioned on the counter with the camera facing Stanley's usual point of entry and the bluetooth speaker placed nearby. The speaker was paired to the Raspberry Pi and chosen as the default audio output.

---

The cat facial recognition was done using OpenCV and a [pre-trained classification model](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml). Start the Python script with:<br>
`$ python3 catFaceDetection.py`<br>
This enables the video feed from the Raspberry Pi Camera Module, and each frame is individually processed by the program for facial recognition. When a cat face is detected, the vacuum noise plays through the Bluetooth speaker to ward the cat away, and a photo is captured. A rectangle is drawn around the cat's face, and the photo is saved locally then uploaded to Cloud storage provider Cloudinary. Using the Vonage API, an SMS text message is then sent to my phone with the newly uploaded photo's URL.

