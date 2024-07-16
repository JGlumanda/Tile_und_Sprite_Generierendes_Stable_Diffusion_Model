import cv2
import matplotlib.pyplot as plt
import numpy as np


def median_filter_interpolation(image, scale):
    original_height, original_width = image.shape[:2]

    new_height = int(original_height * scale)
    new_width = int(original_width * scale)

    new_image = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    kernel_size = int(1 / scale)
    if kernel_size % 2 == 0:
        kernel_size += 1

    for i in range(new_height):
        for j in range(new_width):
            original_x_start = int(i / scale)
            original_y_start = int(j / scale)
            original_x_end = min(original_x_start + kernel_size, original_height)
            original_y_end = min(original_y_start + kernel_size, original_width)

            region = image[original_x_start:original_x_end, original_y_start:original_y_end]

            new_image[i, j] = np.median(region, axis=(0, 1))

    return new_image


image_path = 'img_1.png'
image = cv2.imread(image_path)

scale_factor = 16 / 512

downscaled_image = median_filter_interpolation(image, scale_factor)

downscaled_image_path = 'downscaled_image_median.jpg'
cv2.imwrite(downscaled_image_path, downscaled_image)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Downscaled Image (Median Filter)')
plt.imshow(cv2.cvtColor(downscaled_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()

print(f"Downscaled image saved as {downscaled_image_path}")
