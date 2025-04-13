import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import { Container, Row, Col, Alert, Button, Spinner } from "react-bootstrap";
import axios from "axios";
import "../styles/FileUpload.css";

const FileUploadComponent = () => {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("");
  const [uploading, setUploading] = useState(false);
  const [uploadError, setUploadError] = useState(null);
  const [uploadSuccess, setUploadSuccess] = useState(false);

  const onDrop = (acceptedFiles) => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
      setFileName(acceptedFiles[0].name);
      setUploadSuccess(false);
      setUploadError(null);
    }
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: ".pdf",
  });

  const handleUpload = async () => {
    if (!file) return;
    setUploading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "https://resumesage-backend-v3-production.up.railway.app/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      setUploading(false);
      setUploadSuccess(true);
      console.log(response.data);
    } catch (error) {
      setUploading(false);
      setUploadError(error.message);
    }
  };

  return (
    <Container className="file-upload-box" bg="dark">
      <Row>
        <Col>
          <div
            {...getRootProps()}
            className={`dropzone ${isDragActive ? "dropzone-active" : ""}`}
          >
            <input {...getInputProps()} />
            {fileName ? (
              <Alert variant="success">{fileName}</Alert>
            ) : (
              <Alert variant="secondary">
                {isDragActive
                  ? "Drop the files here..."
                  : "Drag 'n' drop your Resume here, or click to select file."}
              </Alert>
            )}
          </div>
        </Col>
      </Row>
      <Row className="mt-3">
        <Col className="text-center">
          <Button
            onClick={handleUpload}
            disabled={!file || uploading}
            className="btn btn-secondary"
          >
            {uploading ? (
              <Spinner as="span" animation="border" size="sm" />
            ) : (
              "Submit"
            )}
          </Button>
        </Col>
      </Row>
      {uploadError && (
        <Row className="mt-3">
          <Col>
            <Alert variant="danger">{uploadError}</Alert>
          </Col>
        </Row>
      )}
      {uploadSuccess && (
        <div>
          <Row className="mt-3">
            <Col>
              <Alert variant="success">File uploaded successfully!</Alert>
            </Col>
          </Row>
          <h6 className="my-2">
            View your <a href="/summarize"> Resume Summary </a> or view how well
            your <a href="/score">Resume fits </a> with the Job you aim for!
          </h6>
        </div>
      )}
    </Container>
  );
};

export default FileUploadComponent;
