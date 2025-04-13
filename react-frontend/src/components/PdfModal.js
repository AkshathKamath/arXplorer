import React from "react";
import { Modal, Button } from "react-bootstrap";

const PdfViewerModal = ({ show, onHide, pdfUrl }) => {
  return (
    <Modal
      show={show}
      onHide={onHide}
      size="lg"
      aria-labelledby="pdf-viewer-modal"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="pdf-viewer-modal" style={{ color: "#36454F" }}>
          Resume
        </Modal.Title>
      </Modal.Header>
      <Modal.Body style={{ height: "80vh" }}>
        <iframe
          src={pdfUrl}
          title="PDF Viewer"
          style={{ width: "100%", height: "100%" }}
        ></iframe>
      </Modal.Body>
    </Modal>
  );
};

export default PdfViewerModal;
