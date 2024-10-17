import os
from datasets import load_dataset
import helper_utils as utils
import matplotlib.pyplot as plt
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
import json
from datasets import load_dataset
from ultralytics import YOLO
from fastapi import FastAPI
print(tf.__version__)

# Load a YOLOv8 model pre-trained on COCO
model = YOLO("/home/omar/TUM/05_projects/2D-Object-Detection/runs/detect/football_yolov83/weights/last.pt")  # 'n' stands for nano, 's', 'm', 'l'.

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/to_be_predicted")
async def predict_object(image_path: str):
    tmp_folder = "/home/omar/TUM/05_projects/2D-Object-Detection/tmp"
    if not os.path.exists(tmp_folder):  #check if the directory already exists

        os.makedirs(tmp_folder, exist_ok=True)    
   # results = model(image_path)
   # result = results[0]
    result = model(image_path, save=True, project=tmp_folder, name="inference", exist_ok=True)

    #result.save(tmp_folder, result)
    return {"message": "results are saved"}
