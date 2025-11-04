import cv2
import numpy as np

# Create a blank black image (500x300 pixels)
height = 500
width = 500
img = np.zeros((height, width, 3), dtype=np.uint8)

# Define rectangle parameters (green filled rectangle)
rect_top_left = (150, 150)  # (x, y)
rect_bottom_right = (350, 250)  # (x, y)
rect_color = (0, 255, 0)  # Green in BGR

# Draw filled rectangle manually (without cv2.rectangle)
for y in range(rect_top_left[1], rect_bottom_right[1] + 1):
    for x in range(rect_top_left[0], rect_bottom_right[0] + 1):
        if 0 <= y < height and 0 <= x < width:
            img[y, x] = rect_color

# Draw diagonal manually from top-left to bottom-right of ENTIRE IMAGE
# Using Bresenham's line algorithm
x1, y1 = 0, 0
x2, y2 = width - 1, height - 1
diagonal_color = (255, 0, 0)  # Blue in BGR
diagonal_thickness = 2

dx = abs(x2 - x1)
dy = abs(y2 - y1)
sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1
err = dx - dy

x, y = x1, y1

while True:
    # Draw thick line by drawing surrounding pixels
    for dt in range(-diagonal_thickness//2, diagonal_thickness//2 + 1):
        for dt2 in range(-diagonal_thickness//2, diagonal_thickness//2 + 1):
            px, py = x + dt, y + dt2
            if 0 <= py < height and 0 <= px < width:
                img[py, px] = diagonal_color
    
    if x == x2 and y == y2:
        break
    
    e2 = 2 * err
    if e2 > -dy:
        err -= dy
        x += sx
    if e2 < dx:
        err += dx
        y += sy

# Display the image
cv2.imshow("Rectangle and Diagonal", img)
print("Press any key in the image window to close.")

# Wait for key press and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()

# Optional: Save the image
cv2.imwrite("rectangle_diagonal.jpg", img)