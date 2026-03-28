import cv2

image = cv2.imread("images.jpg")

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    choice = input("Enter your choice (save/show): ")
    if choice.lower()=="show":
        title = input("Enter image title: ")
        cv2.imshow(title,gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("Image shown succesfully")
    elif choice.lower()=="save":
        file_name = input("Enter file name with formate(.png/.jpg): ")
        cv2.imwrite(file_name,gray)
        print("Image saved succesfully")
    else:
        print("Please enter valid choice")
else:
    print("Could not able to load the image")