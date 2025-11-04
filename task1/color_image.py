import cv2
import sys
import os
import numpy as np

# Image size (height, width)
H, W = 500, 300

# Create BGR images
red = np.zeros((H, W, 3), dtype=np.uint8)
red[:] = (0, 0, 255)    # BGR -> Red

green = np.zeros((H, W, 3), dtype=np.uint8)
green[:] = (0, 255, 0)  # BGR -> Green

blue = np.zeros((H, W, 3), dtype=np.uint8)
blue[:] = (255, 0, 0)   # BGR -> Blue

# Save images
out_dir = os.getcwd()
cv2.imwrite(os.path.join(out_dir, "red.png"), red)
cv2.imwrite(os.path.join(out_dir, "green.png"), green)
cv2.imwrite(os.path.join(out_dir, "blue.png"), blue)

print(f"Saved: {os.path.join(out_dir, 'red.png')}")
print(f"Saved: {os.path.join(out_dir, 'green.png')}")
print(f"Saved: {os.path.join(out_dir, 'blue.png')}")

# Optionally display one (uncomment to view)
# cv2.imshow("Red", red)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# filepath: /Users/sopen/Documents/Image_lab1/task1/color_image.py
import cv2
import sys
import os
import numpy as np

# ...existing code...

# Image size (height, width)
H, W = 500, 300

# Create BGR images
red = np.zeros((H, W, 3), dtype=np.uint8)
red[:] = (0, 0, 255)    # BGR -> Red

green = np.zeros((H, W, 3), dtype=np.uint8)
green[:] = (0, 255, 0)  # BGR -> Green

blue = np.zeros((H, W, 3), dtype=np.uint8)
blue[:] = (255, 0, 0)   # BGR -> Blue

# Save images
out_dir = os.getcwd()
cv2.imwrite(os.path.join(out_dir, "red.png"), red)
cv2.imwrite(os.path.join(out_dir, "green.png"), green)
cv2.imwrite(os.path.join(out_dir, "blue.png"), blue)

print(f"Saved: {os.path.join(out_dir, 'red.png')}")
print(f"Saved: {os.path.join(out_dir, 'green.png')}")
print(f"Saved: {os.path.join(out_dir, 'blue.png')}")

# Optionally display one (uncomment to view)
# cv2.imshow("Red", red)
# cv2.waitKey(0)
# cv2.destroyAllWindows()