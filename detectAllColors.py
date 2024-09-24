from ColorClass import Color
import colorConstants
import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

while (1):
    # Read per frame from webcam
    _, imageFrame = webcam.read()

    # Convert BGR color space to HSV
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Get all color masks and assign them to contours
    kernel = np.ones((5, 5), "uint8")

    for color in colorConstants.ONE_COLORS:
        mask = cv2.dilate(cv2.inRange(hsvFrame, color.getLowRange(), color.getHighRange()), kernel)
        res_color = cv2.bitwise_and(imageFrame, imageFrame, mask=mask)

        # Find contours
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)

            if (area > 200):
                x, y, width, height = cv2.boundingRect(contour)
                imageFrame = cv2.rectangle(imageFrame, (x, y), (x + width, y + height), (191, 87, 0), 2)
                cv2.putText(imageFrame, f"Detected: {color.getName()}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (191, 87, 0))
    
    cv2.imshow("Multiple Color Detection in Real-Time", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    """
    red_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.RED.getLowRange(), colorConstants.RED.getHighRange()), kernel)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=red_mask)

    red_dupe_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.RED_DUPE.getLowRange(), colorConstants.RED_DUPE.getHighRange()), kernel)
    res_red_dupe = cv2.bitwise_and(imageFrame, imageFrame, mask=red_dupe_mask)

    orange_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.ORANGE.getLowRange(), colorConstants.ORANGE.getHighRange()), kernel)
    res_orange = cv2.bitwise_and(imageFrame, imageFrame, mask=orange_mask)

    brown_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.BROWN.getLowRange(), colorConstants.BROWN.getHighRange()), kernel)
    res_brown = cv2.bitwise_and(imageFrame, imageFrame, mask=brown_mask)

    yellow_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.YELLOW.getLowRange(), colorConstants.YELLOW.getHighRange()), kernel)
    res_yellow = cv2.bitwise_and(imageFrame, imageFrame, mask=yellow_mask)

    lime_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.LIME.getLowRange(), colorConstants.LIME.getHighRange()), kernel)
    res_lime = cv2.bitwise_and(imageFrame, imageFrame, mask=lime_mask)

    green_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.GREEN.getLowRange(), colorConstants.GREEN.getHighRange()), kernel)
    res_green = cv2.bitwise_and(imageFrame, imageFrame, mask=green_mask)

    cyan_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.CYAN.getLowRange(), colorConstants.CYAN.getHighRange()), kernel)
    res_cyan = cv2.bitwise_and(imageFrame, imageFrame, mask=cyan_mask)

    teal_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.TEAL.getLowRange(), colorConstants.TEAL.getHighRange()), kernel)
    res_teal = cv2.bitwise_and(imageFrame, imageFrame, mask=teal_mask)

    blue_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.BLUE.getLowRange(), colorConstants.BLUE.getHighRange()), kernel)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask=blue_mask)

    indigo_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.INDIGO.getLowRange(), colorConstants.INDIGO.getHighRange()), kernel)
    res_indigo = cv2.bitwise_and(imageFrame, imageFrame, mask=indigo_mask)

    purple_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.PURPLE.getLowRange(), colorConstants.PURPLE.getHighRange()), kernel)
    res_purple = cv2.bitwise_and(imageFrame, imageFrame, mask=purple_mask)

    violet_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.VIOLET.getLowRange(), colorConstants.VIOLET.getHighRange()), kernel)
    res_violet = cv2.bitwise_and(imageFrame, imageFrame, mask=violet_mask)

    pink_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.PINK.getLowRange(), colorConstants.PINK.getHighRange()), kernel)
    res_pink = cv2.bitwise_and(imageFrame, imageFrame, mask=pink_mask)

    rose_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.ROSE.getLowRange(), colorConstants.ROSE.getHighRange()), kernel)
    res_rose = cv2.bitwise_and(imageFrame, imageFrame, mask=rose_mask)

    black_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.BLACK.getLowRange(), colorConstants.BLACK.getHighRange()), kernel)
    res_black = cv2.bitwise_and(imageFrame, imageFrame, mask=black_mask)

    white_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.WHITE.getLowRange(), colorConstants.WHITE.getHighRange()), kernel)
    res_white = cv2.bitwise_and(imageFrame, imageFrame, mask=white_mask)

    gray_mask = cv2.dilate(cv2.inRange(hsvFrame, colorConstants.GRAY.getLowRange(), colorConstants.GRAY.getHighRange()), kernel)
    res_grey = cv2.bitwise_and(imageFrame, imageFrame, mask=gray_mask)
    """
