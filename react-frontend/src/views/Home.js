import React, { useState } from "react";
import "../App.css";
import { Container } from "react-bootstrap";
import axios from "axios";
import SearchForm from "./SearchForm";
import PaperCard from "./PaperCard";

const HomePage = () => {
  const [title, setTitle] = useState("");
  const [papers, setPapers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    setPapers([]);
    setError("");

    try {
      const response = await axios.post("http://localhost:4000/search_papers/", {
        title: title,
      });

      setPapers(response.data.papers || []);
    } catch (err) {
      console.error(err);
      setError("Failed to fetch papers. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="mx-4 my-4" style={{ minHeight: "100vh", backgroundColor: "#f5f7fa" }}>
      <Container className="pt-5 d-flex flex-column align-items-center">
        <h3 className="mb-4">Find Research Papers using arXiv API</h3>

        <SearchForm title={title} setTitle={setTitle} handleSearch={handleSearch} loading={loading} />

        {error && <p className="text-danger mt-3">{error}</p>}

        {papers.length > 0 && (
          <div className="mt-5 w-100 d-flex flex-column align-items-center">
            <h5 className="mb-3">Results:</h5>
            {papers.map((paper, idx) => (
              <PaperCard key={idx} title={paper.title} link={paper.link} />
            ))}
          </div>
        )}
      </Container>
    </div>
  );
};

export default HomePage;
