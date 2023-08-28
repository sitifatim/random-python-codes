import cv2
import numpy as np
#define image path to read
image = cv2.imread('random/dataset/happy people/Image_3.jpg')


#reshape image
image = cv2.resize(image,(480,400),interpolation=cv2.INTER_AREA)
#image shape
print(image.shape)
#draw rectangle
cv2.rectangle(image,(44,44),(62,62),(1,1,1),2)
#draw polygon
cv2.polylines(image, [np.array([[13, 13], [75, 13], [75, 75.], [13, 75]],np.int32)],True, (1,1,1),2)
#show the image
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
