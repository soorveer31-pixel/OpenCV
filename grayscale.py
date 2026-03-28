import cv2

image = cv2.imread("images.jpg")

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScale Image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # if gray:
    #     print("Image succesfully converted to gray")
    # else:
    #     print("Somthing went wrong!!")
else:
    print("Could not able to load the image")