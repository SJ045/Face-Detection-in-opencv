import cv2

image=cv2.imread("img.jpg")

gray_image= cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

cv2.imshow("Image", image)

cv2.imshow("Gray_Image", gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()