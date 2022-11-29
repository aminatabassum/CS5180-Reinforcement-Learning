import cv2
 
img = cv2.imread('/home/amina/Downloads/pa1/data/00153v.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 2 # percent of original size
width = int(img.shape[1] * 1 / scale_percent)
height = int(img.shape[0] * 1 / scale_percent)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()