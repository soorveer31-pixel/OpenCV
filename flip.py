import cv2

image = cv2.imread("images.jpg")

if image is not None:
    flipped = cv2.flip(image,1)
    cv2.imshow("Flipped Image",flipped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not loaded")