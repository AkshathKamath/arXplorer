import React, { useState, useEffect } from "react";
import axios from "axios";
import { Container, Card, Spinner } from "react-bootstrap";
import "../App.css";
import NavbarComponent from "../components/Navbar";

const SummaryPage = () => {
  const [data, setData] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "https://resumesage-backend-v3-production.up.railway.app/summarize"
        );
        setData(response.data);
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
        <h3>Your Resume Summary:</h3>
        {loading ? (
          <Spinner animation="border" />
        ) : (
          <Card
            className="mt-3"
            style={{
              backgroundColor: "#36454F",
              border: "1px solid white",
              color: "white",
              borderRadius: "0.25rem",
            }}
          >
            <Card.Body>
              <Card.Text>{data.summary}</Card.Text>
            </Card.Body>
          </Card>
        )}
        {loading ? (
          <p></p>
        ) : (
          <h6 className="my-2">
            Use this as the "Summary" section in your Resume. You can also use
            it as your{" "}
            <a
              href="https://www.linkedin.com/"
              target="_blank"
              rel="noopener noreferrer"
            >
              {" "}
              LinkedIn{" "}
            </a>{" "}
            bio!
          </h6>
        )}
      </Container>
    </div>
  );
};

export default SummaryPage;
