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
magnitude = np.sqrt(filtered_x**2 + filtered_y**2)
orientation = np.arctan2(filtered_y, filtered_x) * 180 / np.pi

# Divide the image into cells of size NxN
N = 16
cells = [img[i:i+N, j:j+N] for i in range(0, img.shape[0], N) for j in range(0, img.shape[1], N)]

# Construct a histogram for each cell
histograms = []
for cell in cells:
    # Create the histogram with 9 bins
    histogram = np.zeros(9)
    for i in range(cell.shape[0]):
        for j in range(cell.shape[1]):
            # Get the orientation of the current pixel and bin it in the histogram
            bin = orientation[i, j] // 20 + 4
            histogram[bin] += magnitude[i, j]
    # Normalize the histogram by the Euclidean norm of the 9 values
    histogram /= np.sqrt(np.sum(histogram**2))
    histograms.append(histogram)

# Concatenate all the histograms to obtain the feature vector
feature_vector = np.concatenate(histograms)


##############

