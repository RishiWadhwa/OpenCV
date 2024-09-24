# Imports
from ColorClass import Color
import colorConstants
import cv2
import numpy as np

# Initialize default webcam (webcam 0 is the computer default webcam whether internal or external)
webcam = cv2.VideoCapture(0)

while (1):
    # Read per frame from webcam
    _, imageFrame = webcam.read()

    # Convert BGR color space to HSV
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Get all color masks and assign them to contours
    kernel = np.ones((5, 5), "uint8")

    # FOR EACH color in COLORS
    for color in colorConstants.ONE_COLORS:
        # Create a mask for the color
        mask = cv2.dilate(cv2.inRange(hsvFrame, color.getLowRange(), color.getHighRange()), kernel)
        res_color = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

        # Find contours
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)

            # Ensures it can't mark a bunch of small finds, needs to be a reasonable size
            if (area > 200):
                x, y, width, height = cv2.boundingRect(contour)
                imageFrame = cv2.rectangle(imageFrame, (x, y), (x + width, y + height), (191, 87, 0), 2)
                cv2.putText(imageFrame, f"Detected: {color.getName()}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (191, 87, 0))
    
    # Window title
    cv2.imshow("Multiple Color Detection in Real-Time", imageFrame)
    
    # Window closes after 10 seconds IFF you press character 'q' on keyboard (keybind 'q' to quit)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
