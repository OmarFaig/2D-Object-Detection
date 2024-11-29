"""
Helper functions for loading images, visualizing bounding boxes, and converting annotations for object detection tasks.

This script includes utility functions to:
- Load images and their associated bounding box annotations.
- Visualize bounding boxes on images using either OpenCV or Matplotlib.
- Draw bounding boxes directly onto images using the Python Imaging Library (PIL).
- Convert bounding box annotations from a JSON format to YOLO format for training object detection models.

Functions:
---------
- vis_bbox(img, bboxes):
    Displays an image with bounding boxes using OpenCV.
    Args:
        img (PIL.Image or NumPy array): The input image in RGB format.
        bboxes (list of lists): List of bounding boxes, where each bounding box is [xmin, ymin, width, height].

- visualize_image_with_bboxes(image, bboxes):
    Visualizes bounding boxes on an image using Matplotlib.
    Args:
        image (PIL.Image): The input image.
        bboxes (list of lists): List of bounding boxes, where each bounding box is [xmin, ymin, width, height].

- load_image_and_annotations(image_path, annotation_path):
    Loads an image and its associated annotations from a JSON file.
    Args:
        image_path (str): Path to the image file.
        annotation_path (str): Path to the JSON file containing annotations.
    Returns:
        Tuple (PIL.Image, list, list): A tuple containing the loaded image, a list of bounding boxes, and labels.

- draw_bounding_boxes(image, bboxes):
    Draws bounding boxes on an image using PIL.
    Args:
        image (PIL.Image): The input image.
        bboxes (list of lists): List of bounding boxes, where each bounding box is [xmin, ymin, width, height].
    Returns:
        PIL.Image: The image with bounding boxes drawn.

- convert_to_yolo_format(annotations_dir, output_dir, image_shape):
    Converts bounding box annotations from JSON format to YOLO format.
    Args:
        annotations_dir (str): Directory containing JSON annotation files.
        output_dir (str): Directory to save the converted YOLO format files.
        image_shape (tuple): Shape of the images as (width, height).

Dependencies:
-------------
- os
- json
- PIL (Pillow)
- numpy
- cv2 (OpenCV)
- matplotlib
"""

import os
import json
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import patches

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
        cv2.rectangle(image_bgr, (int(xmin), int(ymin)),
                       (int(xmax), int(ymax)), (0, 255, 0), 2)  # Draw rectangle in green


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
        rect = patches.Rectangle((xmin, ymin), width, height, 
                                 linewidth=2, edgecolor='r', facecolor='none')
        # Add the rectangle to the plot
        ax.add_patch(rect)

    plt.axis('off')  # Hide the axis
    plt.show()  # Display the plot

def load_image_and_annotations(image_path, annotation_path):
    # Load image
    image = Image.open(image_path).convert("RGB")
    # Load annotation (bounding boxes and labels)
    with open(annotation_path, 'r') as f:
        annotations = json.load(f)
        
    bboxes = annotations['bboxes']  # list of [xmin, ymin, xmax, ymax] in normalized format
    labels = annotations['object_id']  # category labels
    
    return image, bboxes, labels

def draw_bounding_boxes(image, bboxes):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    
    for bbox in bboxes:
      #xmin, ymin, xmax, ymax = bbox
        xmin, ymin, width, height = bbox
        xmax = xmin + width
        ymax = ymin + height
       # print(bbox)
      # # Convert normalized bbox coordinates to absolute pixel coordinates
      # xmin *= width
      # xmax *= width
      # ymin *= height
      # ymax *= height
      # 
        # Draw the bounding box
        draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=3)
    return image

def convert_to_yolo_format(annotations_dir, output_dir, image_shape):
    for json_file in os.listdir(annotations_dir):
        if json_file.endswith('.json'):
            with open(os.path.join(annotations_dir, json_file)) as f:
                annotations = json.load(f)

            image_w, image_h = image_shape
            txt_filename = os.path.splitext(json_file)[0] + '.txt'
            with open(os.path.join(output_dir, txt_filename), 'w') as f:
                for bbox in annotations['bboxes']:
                    x_min, y_min, width, height = bbox

                    # Normalize the bounding box coordinates
                    x_center = (x_min + width / 2) / image_w
                    y_center = (y_min + height / 2) / image_h
                    w = width / image_w
                    h = height / image_h

                    # Write the class and normalized bounding box
                    f.write(f"0 {x_center} {y_center} {w} {h}\n")
