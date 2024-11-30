import React, { useState } from 'react';
import { Container, Row, Col, Card, Button, Modal } from 'react-bootstrap';
import { BsZoomIn } from 'react-icons/bs';  // Import zoom icon
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  const [showModal, setShowModal] = useState(false);
  const [activeTask, setActiveTask] = useState(null);

  const handleZoom = (taskName) => {
    setActiveTask(taskName);
    setShowModal(true);
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
        fullscreen={true}  // This makes it fullscreen
        className="vision-modal"
      >
        <Modal.Header closeButton>
          <Modal.Title>{activeTask}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div className="fullscreen-content">
            <div className="upload-area">
              <input type="file" id="modal-upload" hidden />
              <Button variant="primary" onClick={() => document.getElementById('modal-upload').click()}>
                Upload Image
              </Button>
            </div>
            <div className="fullscreen-results-container">
              <div className="input-section">
                <h4>Input Image</h4>
                <div className="input-image"></div>
              </div>
              <div className="output-section">
                <h4>Result</h4>
                <div className="output-image"></div>
              </div>
            </div>
          </div>
        </Modal.Body>
      </Modal>
    </Container>
  );
}

export default App; 