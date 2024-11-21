# 2D-Object-Detection

This project implements a 2D object detection model using YOLOv8. The model is trained to detect football players and the ball in images.

## Dataset

The dataset used for training the model is a custom football dataset. It contains images of football matches with annotations for football players and the ball. The dataset is organized into three subsets: `train`, `val`, and `test`, each containing images and their corresponding annotations.

## Model

The model used for object detection is YOLOv8 (You Only Look Once version 8). YOLOv8 is a state-of-the-art, real-time object detection system that is fast and accurate. The model is pre-trained on the COCO dataset and fine-tuned on the custom football dataset.

## Setup

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the training script to train the model on the custom dataset:
   ```sh
   python train.py
   ```
2. Use the model for inference to detect objects in new images:
   ```sh
   python main.py
   ```

## Results

Here are some example results from the model:

![Result 1](res/result_1.jpeg)
![Result 2](res/result_2.jpeg)

The model successfully detects football players and the ball in the images, as shown in the results above.
