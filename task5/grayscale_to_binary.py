#!/usr/bin/env python3
"""
Task 5: Convert Grayscale to Binary Image
Location: /Users/sopen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Image_lab1/task5/grayscale_to_binary.py
Description: Load RGB image, convert to grayscale manually, then convert to binary using custom threshold
Why: To demonstrate manual RGB->grayscale->binary conversion without built-in functions
Relevant files: ../test.jpg (input image)
"""

import cv2
import numpy as np
import os

print("Task 5: Convert Grayscale to Binary Image")
print("==========================================")

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

# Step 1: Manual RGB to Grayscale conversion (without cv2.cvtColor)
print("Step 1: Converting RGB to Grayscale manually...")

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

# Step 2: Manual Grayscale to Binary conversion (without cv2.threshold)
print("Step 2: Converting Grayscale to Binary manually...")

# Define custom threshold (middle value of 0-255 range)
threshold = 128
print(f"Using custom threshold: {threshold}")

binary = np.zeros((height, width), dtype=np.uint8)

# Apply manual thresholding
for y in range(height):
    for x in range(width):
        if grayscale[y, x] >= threshold:
            binary[y, x] = 255  # White (above threshold)
        else:
            binary[y, x] = 0    # Black (below threshold)

print(f"Binary conversion completed: {binary.shape}")

# Save both images
grayscale_output = "grayscale_image.jpg"
binary_output = "binary_image.jpg"

cv2.imwrite(grayscale_output, grayscale)
cv2.imwrite(binary_output, binary)

print("Images saved:")
print(f"- Grayscale: {grayscale_output}")
print(f"- Binary: {binary_output}")

print("Task completed successfully!")
