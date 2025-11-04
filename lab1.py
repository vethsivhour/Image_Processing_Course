import cv2
import sys
import os
# Define the image name
image_name = 'test.jpg' # Make sure this file exists in the current folder
# Load the image
image_path = os.path.join(os.getcwd(), image_name)
print(f"Loading image from: {image_path}")
img = cv2.imread(image_path)
# Check if loaded successfully
if img is None:
    print("Error: Could not read the image.")
    print(f"Check that '{image_name}' is in the folder.")
    sys.exit()
# Display image
cv2.imshow("Original Image", img)
cv2.imwrite("output.jpg", img)
print("Press any key in an image window to close.")
# Wait for key press and clean up
cv2.waitKey(0)
cv2.destroyAllWindows()