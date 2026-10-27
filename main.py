import cv2 #opencv library
#load the image
img=cv2.imread("image.png")
#color convesrions
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#DISPLAY THE IMAGES
cv2.imshow("Original Image",img)
cv2.imshow("Gray Image",gray)
cv2.imshow("RGB Image",rgb)
#Keep the window open
cv2.waitKey(0)#0 index of a close button
cv2.destroyAllWindows()