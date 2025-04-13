import React, { useState, useEffect } from "react";
import { Button, Container, Card, Spinner } from "react-bootstrap";
import axios from "axios";
import NavbarComponent from "../components/Navbar";
import PdfViewerModal from "../components/PdfModal";

const ViewPage = () => {
  const [modalShow, setModalShow] = useState(true);
  const [loading, setLoading] = useState(true);
  const [responseData, setResponseData] = useState(null);

  const pdfUrl = "https://resumehelp.s3.amazonaws.com/Resume.pdf";

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "https://resumesage-backend-v3-production.up.railway.app/view"
        );
        setResponseData(response.data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching data:", error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <NavbarComponent />
      <Container className="mt-5">
        <Button variant="secondary" onClick={() => setModalShow(true)}>
          View Resume
        </Button>
        <h5 className="my-2">Improvements:</h5>
        {loading ? (
          <Spinner animation="border" />
        ) : (
          <Card
            className="mt-2"
            style={{
              backgroundColor: "#36454F",
              border: "1px solid white",
              color: "white",
            }}
          >
            <Card.Body>
              <Card.Text>
                <ol>
                  {JSON.parse(responseData.view).map((obj) => (
                    <li>{obj}</li>
                  ))}
                </ol>
              </Card.Text>
            </Card.Body>
          </Card>
        )}
        <PdfViewerModal
          show={modalShow}
          onHide={() => setModalShow(false)}
          pdfUrl={pdfUrl}
        />
      </Container>
    </div>
  );
};

export default ViewPage;
