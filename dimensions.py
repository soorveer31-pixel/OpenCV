import cv2

image = cv2.imread("images.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Image Discription:\nHeight: {h}\nwidth:{w}\nChannel:{c}")
else:
    print("Could not able to load image")