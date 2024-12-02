import React, { useState } from 'react';
import { Container, Row, Col, Card, Button, Modal, Form } from 'react-bootstrap';
import { BsZoomIn } from 'react-icons/bs';  // Import zoom icon
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  const [showModal, setShowModal] = useState(false);
  const [activeTask, setActiveTask] = useState(null);
  const [selectedModel, setSelectedModel] = useState('yolov8n');
  const [bboxColor, setBboxColor] = useState('#FF0000');
  const [confidenceThreshold, setConfidenceThreshold] = useState(0.5);
  const [images, setImages] = useState([]);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [detectionResult, setDetectionResult] = useState(null);

  const handleZoom = (taskName) => {
    setActiveTask(taskName);
    setShowModal(true);
  };

  const handleFolderSelect = (event) => {
    const files = Array.from(event.target.files);
    const imageFiles = files.filter(file => 
      file.type.startsWith('image/')
    );
    
    setImages(imageFiles);
    setCurrentImageIndex(0);
    if (imageFiles.length > 0) {
      processImage(imageFiles[0]);
    }
  };

  const handlePrevious = () => {
    if (currentImageIndex > 0) {
      setCurrentImageIndex(prev => prev - 1);
      processImage(images[currentImageIndex - 1]);
    }
  };

  const handleNext = () => {
    if (currentImageIndex < images.length - 1) {
      setCurrentImageIndex(prev => prev + 1);
      processImage(images[currentImageIndex + 1]);
    }
  };

  const processImage = async (imageFile) => {
    const formData = new FormData();
    formData.append('file', imageFile);

    try {
      const response = await fetch('http://localhost:8000/api/detect', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Detection failed');

      const blob = await response.blob();
      setDetectionResult(URL.createObjectURL(blob));
    } catch (error) {
      console.error('Error during detection:', error);
      // Handle error appropriately
    }
  };

  return (
    <Container fluid className="p-4">
      <h1 className="text-center mb-4">Computer Vision Tasks</h1>
      
      <Row xs={1} md={2} lg={3} className="g-4">
        {/* Object Detection Card */}
        <Col>
          <Card className="h-100">
            <Card.Header className="d-flex justify-content-between align-items-center">
              Object Detection
              <BsZoomIn 
                className="zoom-icon" 
                onClick={() => handleZoom('Object Detection')}
                title="Expand"  // Adds tooltip on hover
              />
            </Card.Header>
            <Card.Body>
              <div className="upload-area">
                <input type="file" id="detection-upload" hidden />
                <Button variant="primary" onClick={() => document.getElementById('detection-upload').click()}>
                  Upload Image
                </Button>
              </div>
              <div className="results-container">
                <div className="input-image"></div>
                <div className="output-image"></div>
              </div>
            </Card.Body>
          </Card>
        </Col>

        {/* Instance Segmentation Card */}
        <Col>
          <Card className="h-100">
            <Card.Header className="d-flex justify-content-between align-items-center">
              Instance Segmentation
              <BsZoomIn 
                className="zoom-icon" 
                onClick={() => handleZoom('Instance Segmentation')}
                title="Expand"  // Adds tooltip on hover
              />
            </Card.Header>
            <Card.Body>
              <div className="upload-area">
                <input type="file" id="segmentation-upload" hidden />
                <Button variant="primary" onClick={() => document.getElementById('segmentation-upload').click()}>
                  Upload Image
                </Button>
              </div>
              <div className="results-container">
                <div className="input-image"></div>
                <div className="output-image"></div>
              </div>
            </Card.Body>
          </Card>
        </Col>

        {/* Semantic Segmentation Card */}
        <Col>
          <Card className="h-100">
            <Card.Header className="d-flex justify-content-between align-items-center">
              Semantic Segmentation
              <BsZoomIn 
                className="zoom-icon" 
                onClick={() => handleZoom('Semantic Segmentation')}
                title="Expand"  // Adds tooltip on hover
              />
            </Card.Header>
            <Card.Body>
              <div className="upload-area">
                <input type="file" id="semantic-upload" hidden />
                <Button variant="primary" onClick={() => document.getElementById('semantic-upload').click()}>
                  Upload Image
                </Button>
              </div>
              <div className="results-container">
                <div className="input-image"></div>
                <div className="output-image"></div>
              </div>
            </Card.Body>
          </Card>
        </Col>

        {/* Object Tracking Card */}
        <Col>
          <Card className="h-100">
            <Card.Header className="d-flex justify-content-between align-items-center">
              Object Tracking
              <BsZoomIn 
                className="zoom-icon" 
                onClick={() => handleZoom('Object Tracking')}
                title="Expand"  // Adds tooltip on hover
              />
            </Card.Header>
            <Card.Body>
              <div className="upload-area">
                <input type="file" id="tracking-upload" hidden accept="video/*" />
                <Button variant="primary" onClick={() => document.getElementById('tracking-upload').click()}>
                  Upload Video
                </Button>
              </div>
              <div className="results-container">
                <div className="input-video"></div>
                <div className="output-video"></div>
              </div>
            </Card.Body>
          </Card>
        </Col> {/* SLAM Card */}
        <Col>
          <Card className="h-100">
            <Card.Header className="d-flex justify-content-between align-items-center">
              SLAM
              <BsZoomIn 
                className="zoom-icon" 
                onClick={() => handleZoom('SLAM')}
                title="Expand"  // Adds tooltip on hover
              />
            </Card.Header>
            <Card.Body>
              <div className="upload-area">
                <input type="file" id="tracking-upload" hidden accept="video/*" />
                <Button variant="primary" onClick={() => document.getElementById('tracking-upload').click()}>
                  Upload Video
                </Button>
              </div>
              <div className="results-container">
                <div className="input-video"></div>
                <div className="output-video"></div>
              </div>
            </Card.Body>
          </Card>
        </Col>
         {/* 3D Object Detection Card  */}
         <Col>
          <Card className="h-100">
            <Card.Header className="d-flex justify-content-between align-items-center">
              3D Object Detection
              <BsZoomIn 
                className="zoom-icon" 
                onClick={() => handleZoom('3D Object Detection')}
                title="Expand"  // Adds tooltip on hover
              />
            </Card.Header>
            <Card.Body>
              <div className="upload-area">
                <input type="file" id="tracking-upload" hidden accept="video/*" />
                <Button variant="primary" onClick={() => document.getElementById('tracking-upload').click()}>
                  Upload Video
                </Button>
              </div>
              <div className="results-container">
                <div className="input-video"></div>
                <div className="output-video"></div>
              </div>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      {/* Fullscreen Modal */}
      <Modal 
        show={showModal} 
        onHide={() => setShowModal(false)}
        fullscreen={true}
        className="vision-modal"
      >
        <Modal.Header closeButton>
          <Modal.Title>{activeTask}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div className="fullscreen-content">
            {/* Detection Options */}
            {activeTask === 'Object Detection' && (
              <div className="detection-options mb-3">
                <h5>Detection Options:</h5>
                <Form>
                  {/* Model Selection */}
                  <Form.Group className="mb-3">
                    <Form.Label>Model</Form.Label>
                    <Form.Select 
                      value={selectedModel}
                      onChange={(e) => setSelectedModel(e.target.value)}
                    >
                      <option value="yolov8n">YOLOv8 Nano</option>
                      <option value="yolov8s">YOLOv8 Small</option>
                      <option value="yolov8m">YOLOv8 Medium</option>
                      <option value="yolov8l">YOLOv8 Large</option>
                      <option value="yolov8x">YOLOv8 XLarge</option>
                    </Form.Select>
                  </Form.Group>

                  {/* Visualization Options */}
                  <Form.Group className="mb-3">
                    <Form.Label>Bounding Box Color</Form.Label>
                    <Form.Control
                      type="color"
                      value={bboxColor}
                      onChange={(e) => setBboxColor(e.target.value)}
                      title="Choose bounding box color"
                    />
                  </Form.Group>

                  {/* Confidence Threshold */}
                  <Form.Group className="mb-3">
                    <Form.Label>Confidence Threshold: {confidenceThreshold}</Form.Label>
                    <Form.Range
                      min={0}
                      max={1}
                      step={0.05}
                      value={confidenceThreshold}
                      onChange={(e) => setConfidenceThreshold(parseFloat(e.target.value))}
                    />
                  </Form.Group>

                  {/* Checkboxes */}
                  <Form.Group className="mb-3">
                    <Form.Check 
                      type="checkbox"
                      id="bbox-checkbox"
                      label="Show Bounding Boxes"
                      defaultChecked
                    />
                    <Form.Check 
                      type="checkbox"
                      id="labels-checkbox"
                      label="Show Labels"
                      defaultChecked
                    />
                    <Form.Check 
                      type="checkbox"
                      id="confidence-checkbox"
                      label="Show Confidence Scores"
                      defaultChecked
                    />
                  </Form.Group>

                  {/* Additional Options */}
                  <Form.Group className="mb-3">
                    <Form.Label>Label Font Size</Form.Label>
                    <Form.Select defaultValue="medium">
                      <option value="small">Small</option>
                      <option value="medium">Medium</option>
                      <option value="large">Large</option>
                    </Form.Select>
                  </Form.Group>

                  {/* Video-specific options */}
                  <Form.Group className="mb-3">
                    <Form.Check 
                      type="checkbox"
                      id="tracking-checkbox"
                      label="Enable Tracking (for videos)"
                    />
                  </Form.Group>
                </Form>
              </div>
            )}
            
            {/* Image Upload and Navigation */}
            <div className="upload-area mb-3">
              <input 
                type="file" 
                id="folder-upload" 
                hidden 
                webkitdirectory="" 
                directory=""
                onChange={handleFolderSelect}
              />
              <Button 
                variant="primary" 
                onClick={() => document.getElementById('folder-upload').click()}
              >
                Select Folder
              </Button>
              
              {images.length > 0 && (
                <div className="navigation-controls mt-2">
                  <Button 
                    variant="secondary" 
                    onClick={handlePrevious}
                    disabled={currentImageIndex === 0}
                  >
                    Previous
                  </Button>
                  <span className="mx-2">
                    Image {currentImageIndex + 1} of {images.length}
                  </span>
                  <Button 
                    variant="secondary" 
                    onClick={handleNext}
                    disabled={currentImageIndex === images.length - 1}
                  >
                    Next
                  </Button>
                </div>
              )}
            </div>

            {/* Results Display */}
            <div className="fullscreen-results-container">
              <div className="input-section">
                <h4>Input Image</h4>
                {images.length > 0 && (
                  <img 
                    src={URL.createObjectURL(images[currentImageIndex])}
                    alt="Input"
                    style={{ maxWidth: '100%', height: 'auto' }}
                  />
                )}
              </div>
              <div className="output-section">
                <h4>Detection Result</h4>
                {detectionResult && (
                  <img 
                    src={detectionResult}
                    alt="Detection Result"
                    style={{ maxWidth: '100%', height: 'auto' }}
                  />
                )}
              </div>
            </div>
          </div>
        </Modal.Body>
      </Modal>
    </Container>
  );
}

export default App; 