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
from fastapi import FastAPI, Form,File,UploadFile
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import shutil
print(tf.__version__)

# Load a YOLOv8 model pre-trained on COCO
model = YOLO("/home/omar/TUM/05_projects/2D-Object-Detection/runs/detect/football_yolov83/weights/last.pt")  # 'n' stands for nano, 's', 'm', 'l'.

app = FastAPI()
# Serve static files like your HTML, CSS, JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Return the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_home():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())


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

# Route for uploading images
@app.post("/upload-images")
async def upload_images(files: List[UploadFile] = File(...)):
    # Save uploaded images to a folder (e.g., 'uploaded_images/')
    upload_folder = "tmp/inference/"
    for file in files:
        file_location = f"{upload_folder}{file.filename}"
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    
    # Return a response indicating successful upload
    return JSONResponse({"message": f"Successfully uploaded {len(files)} files"})