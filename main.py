from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import numpy as np
import uvicorn
from ultralytics import YOLO
import os
from typing import Dict

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model - you might want to make this configurable
models: Dict[str, YOLO] = {}

@app.post("/api/detect")
async def detect(
    file: UploadFile = File(...),
    model_name: str = Form("yolov8n"),
    conf_threshold: float = Form(0.25),
    bbox_color: str = Form("#FF0000"),
    label_size: str = Form("medium")
):
    try:
        print(f"Received parameters: model={model_name}, conf={conf_threshold}, color={bbox_color}")
        
        # Load or get model
        if model_name not in models:
            model_path = f"{model_name}.pt"
            print(f"Loading model from {model_path}")
            models[model_name] = YOLO(model_path)
        current_model = models[model_name]
        
        # Read and validate the image
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Run inference with user-specified confidence
        results = current_model(image, conf=float(conf_threshold))
        result = results[0]
        
        # Set font size based on label_size parameter
        font_sizes = {"small": 10, "medium": 12, "large": 16}
        font_size = font_sizes.get(label_size, 12)
        
        # Create a copy of the image for drawing
        output_image = image.copy()
        draw = ImageDraw.Draw(output_image)
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()

        # Draw detections
        if hasattr(result, 'boxes') and result.boxes is not None:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = [int(x) for x in box.xyxy[0]]
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                class_name = result.names[cls]
                
                # Use user-specified color
                draw.rectangle([x1, y1, x2, y2], outline=bbox_color, width=2)
                
                label = f"{class_name} {conf:.2f}"
                text_bbox = draw.textbbox((x1, y1), label, font=font)
                draw.rectangle(text_bbox, fill=bbox_color)
                draw.text((x1, y1), label, fill="white", font=font)

        # Save and return the image
        output_buffer = BytesIO()
        output_image.save(output_buffer, format="JPEG", quality=95)
        output_buffer.seek(0)
        
        return StreamingResponse(output_buffer, media_type="image/jpeg")
        
    except Exception as e:
        print(f"Error in detection: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Add endpoint to get available models
@app.get("/api/models")
async def get_models():
    return {
        "models": [
            "yolov8n",
            "yolov8s",
            "yolov8m",
            "yolov8l",
            "yolov8x"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)