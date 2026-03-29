import cv2

image = cv2.imread("images.jpg")

if image is not None:
    resized = cv2.resize(image,(500,750))
    cv2.imshow("Resized image",resized)
    cv2.imshow("Original Image",image)

    cv2.imwrite("Resized_image.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("COuld not able to load the image")