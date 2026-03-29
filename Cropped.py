import cv2

image = cv2.imread("images.jpg")

if image is not None:
    cropped = image[70:170,50:150]

    cv2.imshow("Cropped image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("COuld not able to load the image")