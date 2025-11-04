#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Task 4: Convert RGB to Grayscale
Location: /Users/sopen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Image_lab1/task4/rgb_to_grayscale.py
Description: Load an RGB image and manually convert it to grayscale without using cv2.cvtColor()
Why: To demonstrate manual RGB to grayscale conversion using luminance formula
Relevant files: ../test.jpg (input image)
"""

import cv2
import numpy as np
import os

print("Task 4: Convert RGB to Grayscale")
print("================================")

# Load the image in BGR format (OpenCV default)
image_path = "../test.jpg"
print(f"Loading image from: {os.path.abspath(image_path)}")

img_bgr = cv2.imread(image_path)
if img_bgr is None:
    print(f"Error: Could not load image from {image_path}")
    exit(1)

print(f"Image loaded successfully: {img_bgr.shape}")

# Convert BGR to RGB for processing
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# Manual RGB to Grayscale conversion (without cv2.cvtColor)
print("Converting RGB to Grayscale manually...")

# Create grayscale image array
height, width = img_rgb.shape[:2]
grayscale = np.zeros((height, width), dtype=np.uint8)

# Use luminance formula: Gray = 0.299*R + 0.587*G + 0.114*B
for y in range(height):
    for x in range(width):
        r, g, b = img_rgb[y, x]
        # Luminance formula for grayscale conversion
        gray_value = 0.299 * r + 0.587 * g + 0.114 * b
        grayscale[y, x] = int(gray_value)

print(f"Grayscale conversion completed: {grayscale.shape}")

# Save the grayscale image
output_path = "grayscale_image.jpg"
cv2.imwrite(output_path, grayscale)

print(f"Grayscale image saved as: {output_path}")
print("Task completed successfully!")
