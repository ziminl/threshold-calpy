from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
pixels = image.reshape(-1, 1)

kmeans = KMeans(n_clusters=2, random_state=0).fit(pixels)
labels = kmeans.labels_.reshape(image.shape)

threshold = kmeans.cluster_centers_.min()
thresholded_image = (image > threshold).astype(np.uint8) * 255

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Thresholded Image')
plt.imshow(thresholded_image, cmap='gray')

plt.show()
