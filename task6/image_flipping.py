#!/usr/bin/env python3
"""
Task 6: Image Flipping (Vertical and Horizontal)
Location: /Users/sopen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Image_lab1/task6/image_flipping.py
Description: Load RGB image and manually flip it vertically and horizontally without cv2.flip()
Why: To demonstrate manual image flipping algorithms and understand OpenCV's BGR format
Relevant files: ../test.jpg (input image)
"""

import cv2
import numpy as np
import os

print("Task 6: Image Flipping (Vertical and Horizontal)")
print("================================================")

# Load the image in BGR format (OpenCV default)
image_path = "../test.jpg"
print(f"Loading image from: {os.path.abspath(image_path)}")

img_bgr = cv2.imread(image_path)
if img_bgr is None:
    print(f"Error: Could not load image from {image_path}")
    exit(1)

print(f"Image loaded successfully: {img_bgr.shape} (BGR format)")

# Convert BGR to RGB for processing
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
print(f"Converted to RGB format: {img_rgb.shape}")

height, width = img_rgb.shape[:2]

# Step 1: Manual Vertical Flip (upside down)
print("Step 1: Creating vertical flip manually...")

vertical_flip = np.zeros_like(img_rgb)

for y in range(height):
    for x in range(width):
        # Vertical flip: pixel at (x, y) goes to (x, height-1-y)
        vertical_flip[height-1-y, x] = img_rgb[y, x]

print(f"Vertical flip completed: {vertical_flip.shape}")

# Step 2: Manual Horizontal Flip (left-right mirror)
print("Step 2: Creating horizontal flip manually...")

horizontal_flip = np.zeros_like(img_rgb)

for y in range(height):
    for x in range(width):
        # Horizontal flip: pixel at (x, y) goes to (width-1-x, y)
        horizontal_flip[y, width-1-x] = img_rgb[y, x]

print(f"Horizontal flip completed: {horizontal_flip.shape}")

# Convert back to BGR for OpenCV saving (since OpenCV expects BGR)
original_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
vertical_bgr = cv2.cvtColor(vertical_flip, cv2.COLOR_RGB2BGR)
horizontal_bgr = cv2.cvtColor(horizontal_flip, cv2.COLOR_RGB2BGR)

# Save all three images
cv2.imwrite("original_rgb.jpg", original_bgr)
cv2.imwrite("vertical_flip.jpg", vertical_bgr)
cv2.imwrite("horizontal_flip.jpg", horizontal_bgr)

print("Images saved:")
print("- original_rgb.jpg (RGB converted back to BGR for OpenCV)")
print("- vertical_flip.jpg (upside down)")
print("- horizontal_flip.jpg (left-right mirror)")

print("Note: All images saved in BGR format as expected by OpenCV")
print("Task completed successfully!")
