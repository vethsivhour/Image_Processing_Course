#!/usr/bin/env python3
"""
Task 3: Split Image Channels
Location: /Users/sopen/Library/Mobile Documents/com~apple~CloudDocs/Documents/Image_lab1/task3/split_channels.py
Description: Load an image and manually split it into Red, Green, and Blue channel images
Why: To demonstrate manual channel splitting without using cv2.split()
Relevant files: ../test.jpg (input image)
"""

import cv2
import numpy as np
import os

print("Task 3: Split Image Channels")
print("============================")

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

# Manual channel splitting (without cv2.split)
print("Splitting channels manually...")

# Red channel: R, 0, 0
red_channel = np.zeros_like(img_rgb)
red_channel[:, :, 0] = img_rgb[:, :, 0]

# Green channel: 0, G, 0
green_channel = np.zeros_like(img_rgb)
green_channel[:, :, 1] = img_rgb[:, :, 1]

# Blue channel: 0, 0, B
blue_channel = np.zeros_like(img_rgb)
blue_channel[:, :, 2] = img_rgb[:, :, 2]

# Convert back to BGR for OpenCV saving
red_bgr = cv2.cvtColor(red_channel, cv2.COLOR_RGB2BGR)
green_bgr = cv2.cvtColor(green_channel, cv2.COLOR_RGB2BGR)
blue_bgr = cv2.cvtColor(blue_channel, cv2.COLOR_RGB2BGR)

# Save the images
output_dir = "."
cv2.imwrite("red_channel.jpg", red_bgr)
cv2.imwrite("green_channel.jpg", green_bgr)
cv2.imwrite("blue_channel.jpg", blue_bgr)

print("Channel images saved:")
print("- red_channel.jpg")
print("- green_channel.jpg")
print("- blue_channel.jpg")

print("Task completed successfully!")
