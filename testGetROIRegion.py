import cv2
import numpy as np


# Load the reference image
image_path = "C:\\Users\\naimu\\OneDrive - London South Bank University\\Pictures\\myimage2.jpg"
image = cv2.imread(image_path)

import cv2

# Load the image
image = cv2.imread('path/to/your/image.jpg')

# Display the image
cv2.imshow('Image', image)

# Select ROI using cv2.selectROI()
roi = cv2.selectROI(image)

# Crop the selected ROI from the image
roi_cropped = image[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]

# Display the cropped ROI
cv2.imshow('Cropped ROI', roi_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Get ROI coordinates
roi_x, roi_y, roi_width, roi_height = roi
print(f"ROI Coordinates: x={roi_x}, y={roi_y}, width={roi_width}, height={roi_height}")
