import cv2
import numpy as np
from matplotlib import pyplot as plt


image_bgr = cv2.imread(r'C:\Users\Nizam\Desktop\recomendationsystem\image_preprocessing\images.jpeg')
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
# Rectangle values: start x, start y, width, height
rectangle = (0, 56, 256, 150)
# Create initial mask
mask = np.zeros(image_rgb.shape[:2], np.uint8)
# Create temporary arrays used by grabCut
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)


cv2.grabCut(image_rgb, # Our image
 mask, # The Mask
 rectangle, # Our rectangle
 bgdModel, # Temporary array for background
 fgdModel, # Temporary array for background
 5, # Number of iterations
 cv2.GC_INIT_WITH_RECT) # Initiative using our rectangle
# Create mask where sure and likely backgrounds set to 0, otherwise 1
mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
# Multiply image with new mask to subtract background
image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]
# Show image
plt.imshow(image_rgb_nobg), plt.axis("off")
plt.show()


#need to explore it more

#159