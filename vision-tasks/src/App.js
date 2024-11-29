import React from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  return (
    <Container fluid className="p-4">
      <h1 className="text-center mb-4">Computer Vision Tasks</h1>
      
      <Row xs={1} md={2} lg={3} className="g-4">
        {/* Object Detection Card */}
        <Col>
          <Card className="h-100">
            <Card.Header>Object Detection</Card.Header>
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
            <Card.Header>Instance Segmentation</Card.Header>
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
            <Card.Header>Semantic Segmentation</Card.Header>
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
            <Card.Header>Object Tracking</Card.Header>
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
    </Container>
  );
}

export default App; 