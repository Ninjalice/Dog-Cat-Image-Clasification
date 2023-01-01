# Import the necessary modules
import cv2
import numpy as np

# Load the image and convert it to grayscale
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply the spatial filter approximation of the partial derivative in the x direction
kernel_x = np.array([[-1, 0, 1]])
filtered_x = cv2.filter2D(img, -1, kernel_x)

# Apply the spatial filter approximation of the partial derivative in the y direction
kernel_y = np.array([[-1], [0], [1]])
filtered_y = cv2.filter2D(img, -1, kernel_y)

# Calculate the gradient magnitude and orientation
m
