import React, { useState, useEffect } from "react";
import "../App.css";
import { Container, Card, Spinner } from "react-bootstrap";
import axios from "axios";
import { useLocation } from "react-router-dom";
import NavbarComponent from "../components/Navbar";

const ViewPage = () => {
  const query = new URLSearchParams(useLocation().search);
  // const title = query.get("title");
  const link = query.get("link");
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState("");

  useEffect(() => {
    uploadPaper();
    fetchSummary();
  }, []);

  const fetchSummary = async () => {
    setLoading(true);
    setSummary("");

    try {
      const response = await axios.post(
        "https://akshathkamath7-arxivsummarizer.hf.space/summarize_paper/",
        {
          url: link,
        }
      );

      setSummary(response.data.summary || "");
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const uploadPaper = async () => {
    try {
      const response = await axios.post(
        "https://arxplorer-production-376d.up.railway.app/store_to_pinecone/",
        {
          url: link,
        }
      );
      console.log(response.data);
    } catch (err) {
      console.error(err);
    } finally {
    }
  };

  return (
    <div>
      <NavbarComponent />
      <Container className="mt-5">
        <h3>Paper Summary</h3>
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
              <Card.Text>{summary}</Card.Text>
            </Card.Body>
          </Card>
        )}
      </Container>
      <Container className="mt-5">
        <h3>QA</h3>
      </Container>
    </div>
  );
};

export default ViewPage;
