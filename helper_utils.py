import os
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
def visualize_image_with_bboxes(image, bboxes):
    # Create a figure and axis
    fig, ax = plt.subplots(1)
    
    # Display the image
    ax.imshow(image)
    
    # Add bounding boxes
    for bbox in bboxes:
        xmin, ymin, width, height = bbox
        # Create a rectangle patch (matplotlib uses (xmin, ymin, width, height))
        rect = patches.Rectangle((xmin, ymin), width, height, linewidth=2, edgecolor='r', facecolor='none')
        # Add the rectangle to the plot
        ax.add_patch(rect)

    plt.axis('off')  # Hide the axis
    plt.show()  # Display the plot