import cv2
#read the image
image=cv2.imread("image.png")
#image shape
print("Width and height",image.shape)
#resize the image
resized_image=cv2.resize(image,(166,316,))
while True:
#display the original image
    cv2.imshow("Original image",image)
#resized image
    cv2.imshow("Resized image",resized_image)
#c-to close the window
    key=cv2.waitKey(1)&0xFF
    if key==ord("c"):
        break
cv2.destroyAllWindows()