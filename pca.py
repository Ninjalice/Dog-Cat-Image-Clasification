# Import the necessary modules
import cv2
import numpy as np

# Load the images and convert them to grayscale
images = [cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE),
          cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE),
          cv2.imread('image3.jpg', cv2.IMREAD_GRAYSCALE)]

# Convert the images to a dataset by flattening each image into a 1D array
X = [image.flatten() for image in images]

# Perform PCA on the dataset
mean, eigenvectors = cv2.PCACompute(X)

# Print the explained variance ratio for each component
print(eigenvectors / np.sum(eigenvectors))

# Reconstruct the images using the first two components
X_reconstructed = mean + eigenvectors[:2] @ X

# Convert the reconstructed images back to their original shape
images_reconstructed = [image.reshape(original_shape) for image in X_reconstructed]
