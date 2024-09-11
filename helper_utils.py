import os
#import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import cv2
def vis_bbox(img,bboxes):
    if isinstance(img, Image.Image):
        image_np = np.array(img)  # Convert PIL image to NumPy array

    # Convert RGB (Matplotlib/PIL) to BGR (OpenCV uses BGR by default)
    image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # Example: Access the bounding boxes for the objects (assuming objects is a list of bboxes)
    print(bboxes)
    # Draw bounding boxes on the image (assuming bboxes is a list of [xmin, ymin, xmax, ymax])
    for bbox in bboxes:
        xmin, ymin, width, height = bbox  # Access elements of the bounding box list
        xmax = xmin + width
        ymax = ymin + height
        cv2.rectangle(image_bgr, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)  # Draw rectangle in green


    # Display the image with bounding boxes using OpenCV
    cv2.imshow("Image with Bounding Boxes", image_bgr)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)
