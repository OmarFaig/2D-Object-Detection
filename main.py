import os
from datasets import load_dataset
import helper_utils as utils
import matplotlib.pyplot as plt
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image,ImageDraw,ImageFont
import json
from datasets import load_dataset
from ultralytics import YOLO
from fastapi import FastAPI, Form,File,UploadFile
from fastapi.responses import HTMLResponse,JSONResponse,StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import shutil
from io import BytesIO

print(tf.__version__)

# Load a YOLOv8 model pre-trained on COCO
model = YOLO("/home/omar/TUM/05_projects/2D-Object-Detection/runs/detect/football_yolov83/weights/last.pt")  # 'n' stands for nano, 's', 'm', 'l'.
#results = model('football_dataset/test/images/7.png')

# Access the first result in the list
#result = results[0]

# Display the results
#result.show()
#result.plot()  # This will plot the results on the image
app = FastAPI()
# Serve static files like your HTML, CSS, JS
app.mount("/static", StaticFiles(directory="static"), name="static")
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],  # specify the origins you want to allow
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Load image in memory
    image_data = await file.read()
    image = Image.open(BytesIO(image_data))

    # Run YOLO on image
    results = model(image, save=False) 
    result = results[0]
    
    # Create ImageDraw object
    draw = ImageDraw.Draw(image)
    # Create a font object (you might need to adjust the size)
    font = ImageFont.truetype("arial.ttf", 16)  # Use a system font
    
    if hasattr(result, 'boxes') and result.boxes is not None:
        boxes = result.boxes
        for box in boxes:
            # Get box coordinates
            x1, y1, x2, y2 = box.xyxy[0]  # Get box coordinates
            
            # Get confidence and class
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            class_name = result.names[cls]  # Get class name from model's names dict
            
            # Draw box
            draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
            
            # Create label with class name and confidence
            label = f"{class_name} {conf:.2f}"
            
            # Draw label background
            text_bbox = draw.textbbox((x1, y1), label, font=font)
            draw.rectangle(text_bbox, fill="blue")
            
            # Draw white text
            draw.text((x1, y1), label, fill="white", font=font)

    # Save the modified image
    response = BytesIO()
    image.save(response, format="JPEG")
    response.seek(0)
    return StreamingResponse(response, media_type="image/jpeg")