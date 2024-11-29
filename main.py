from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import uvicorn
from ultralytics import YOLO
app = FastAPI()

# Add CORS middleware for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Your existing model initialization
model = YOLO("/home/omar/TUM/05_projects/2D-Object-Detection/runs/detect/football_yolov83/weights/last.pt")  # 'n' stands for nano, 's', 'm', 'l'.

@app.post("/api/detect")
async def detect(file: UploadFile = File(...)):
    # Your existing object detection code
    image_data = await file.read()
    image = Image.open(BytesIO(image_data))

    # Run YOLO on image
    results = model(image, save=False) 
    result = results[0]
    
    # Create ImageDraw object
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # or use truetype font if available
    
    if hasattr(result, 'boxes') and result.boxes is not None:
        boxes = result.boxes
        for box in boxes:
            # Get box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            
            # Get confidence and class
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            class_name = result.names[cls]
            
            # Draw box
            draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
            
            # Create label with class name and confidence
            label = f"{class_name} {conf:.2f}"
            
            # Draw label background
            text_bbox = draw.textbbox((x1, y1), label, font=font)
            draw.rectangle(text_bbox, fill="red")
            
            # Draw white text
            draw.text((x1, y1), label, fill="white", font=font)

    # Save and return the image
    response = BytesIO()
    image.save(response, format="JPEG")
    response.seek(0)
    return StreamingResponse(response, media_type="image/jpeg")

@app.post("/api/segment")
async def segment(file: UploadFile = File(...)):
    # Instance segmentation code - implement when needed
    # You'll need a segmentation model like YOLOv8-seg
    pass

@app.post("/api/semantic-segment")
async def semantic_segment(file: UploadFile = File(...)):
    # Semantic segmentation code - implement when needed
    pass

@app.post("/api/track")
async def track(file: UploadFile = File(...)):
    # Object tracking code - implement when needed
    # You'll need a tracking model like YOLOv8-track
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)