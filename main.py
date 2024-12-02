from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import numpy as np
import uvicorn
from ultralytics import YOLO
import os

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
model = YOLO("yolov8n.pt")  # Using the default YOLO model for now

@app.post("/api/detect")
async def detect(file: UploadFile = File(...)):
    try:
        # Read and validate the image
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Run inference
        results = model(image, conf=0.25)  # Adjust confidence threshold as needed
        result = results[0]
        
        # Create a copy of the image for drawing
        output_image = image.copy()
        draw = ImageDraw.Draw(output_image)
        
        # Try to load a better font, fallback to default if not available
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
        except:
            font = ImageFont.load_default()

        # Draw detections
        if hasattr(result, 'boxes') and result.boxes is not None:
            boxes = result.boxes
            for box in boxes:
                # Get box coordinates
                x1, y1, x2, y2 = [int(x) for x in box.xyxy[0]]
                
                # Get confidence and class
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                class_name = result.names[cls]
                
                # Draw box
                draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
                
                # Create label
                label = f"{class_name} {conf:.2f}"
                
                # Get text size
                text_bbox = draw.textbbox((x1, y1), label, font=font)
                
                # Draw label background
                draw.rectangle(
                    [text_bbox[0], text_bbox[1], text_bbox[2], text_bbox[3]],
                    fill="red"
                )
                
                # Draw text
                draw.text((x1, y1), label, fill="white", font=font)

        # Save and return the image
        output_buffer = BytesIO()
        output_image.save(output_buffer, format="JPEG", quality=95)
        output_buffer.seek(0)
        
        return StreamingResponse(
            output_buffer, 
            media_type="image/jpeg",
            headers={
                'Content-Disposition': f'inline; filename="{file.filename}"'
            }
        )
        
    except Exception as e:
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