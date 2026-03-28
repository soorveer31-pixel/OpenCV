import cv2

image = cv2.imread("images.jpg")

if image is not None:
    save = cv2.imwrite("Output_image.png",image)
    if save:
        print("Image saved succesfully")
    else:
        print("Not able to save image")
else:
    print("Error: Could not able to load image")