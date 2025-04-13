import React, { useState } from "react";
import axios from "axios";
import { Container, Card, Spinner, Form, Button } from "react-bootstrap";
import "../App.css";
import NavbarComponent from "../components/Navbar";

const ScorePage = () => {
  const [jobRole, setJobRole] = useState("");
  const [jobDescription, setJobDescription] = useState("");
  const [responseData, setResponseData] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!jobRole || !jobDescription) {
      alert("Both fields are required.");
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post(
        "https://resumesage-backend-v3-production.up.railway.app/score",
        {
          role: jobRole,
          jd: jobDescription,
        }
      );

      setResponseData(response.data);

      console.log("Response:", response.data);
    } catch (error) {
      console.error("Error submitting form:", error);
      alert("Failed to submit form. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const linkedInUrl = `https://www.linkedin.com/jobs/search/?&geoId=103644278&keywords=${encodeURIComponent(
    jobRole
  )}&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true`;

  return (
    <div>
      <NavbarComponent />
      <Container className="mt-5">
        <h3>Job Details</h3>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="formJobRole">
            <Form.Label>Enter Job Role:</Form.Label>
            <Form.Control
              type="text"
              value={jobRole}
              onChange={(e) => setJobRole(e.target.value)}
              className="form"
            />
          </Form.Group>

          <Form.Group controlId="formJobDescription" className="mt-3">
            <Form.Label> Enter Job Description:</Form.Label>
            <Form.Control
              as="textarea"
              rows={5}
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              className="form"
            />
          </Form.Group>

          <Button
            variant="secondary"
            type="submit"
            className="mt-3"
            disabled={loading}
          >
            {loading ? <Spinner animation="border" size="sm" /> : "Submit"}
          </Button>
        </Form>
        {responseData && (
          <div>
            <h5 className="my-2">
              JD-Resume Fit Score: {responseData.score}/10
            </h5>
            <h6 className="my-4">Improvements:</h6>
            <Card
              className="mt-2"
              style={{
                backgroundColor: "#36454F",
                border: "1px solid white",
                color: "white",
              }}
            >
              <Card.Body>
                {/* <Card.Title>Improvements</Card.Title> */}
                <Card.Text>
                  <ol>
                    {JSON.parse(responseData.improvements).map((obj) => (
                      <li>{obj}</li>
                    ))}
                  </ol>
                </Card.Text>
              </Card.Body>
            </Card>
            <h6 className="my-2">
              Apply for {jobRole} roles on{" "}
              <a href={linkedInUrl} target="_blank" rel="noopener noreferrer">
                LinkedIN
              </a>
              !
            </h6>
          </div>
        )}
      </Container>
    </div>
  );
};

export default ScorePage;
