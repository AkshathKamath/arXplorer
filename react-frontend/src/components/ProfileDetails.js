import React, { useState } from "react";
import { Container, Form, Button } from "react-bootstrap";
import "axios";
import "../App.css";

const ProfileForm = () => {
  const [name, setName] = useState("");
  const [school, setSchool] = useState("");
  const [major, setMajor] = useState("");
  const [company, setCompany] = useState("");
  const [linkedin, setLinkedin] = useState("");
  const [twitter, setTwitter] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    // console.log(name, school, major, company, linkedin, twitter);

    setName("");
    setSchool("");
    setMajor("");
    setCompany("");
    setTwitter("");
    setLinkedin("");
  };

  return (
    <div>
      <Container className="mt-5">
        <h5>Enter your details to connect with me!</h5>
        <Form onSubmit={handleSubmit}>
          <Form.Group controlId="formJobRole">
            <Form.Label>Full Name:</Form.Label>
            <Form.Control
              type="text"
              className="form"
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </Form.Group>

          <Form.Group controlId="formJobDescription" className="mt-3">
            <Form.Label>School:</Form.Label>
            <Form.Control
              type="text"
              className="form"
              value={school}
              onChange={(e) => setSchool(e.target.value)}
            />
          </Form.Group>

          <Form.Group controlId="formJobDescription" className="mt-3">
            <Form.Label>Major:</Form.Label>
            <Form.Control
              type="text"
              className="form"
              value={major}
              onChange={(e) => setMajor(e.target.value)}
            />
          </Form.Group>

          <Form.Group controlId="formJobDescription" className="mt-3">
            <Form.Label>Current/Previous Company:</Form.Label>
            <Form.Control
              type="text"
              className="form"
              value={company}
              onChange={(e) => setCompany(e.target.value)}
            />
          </Form.Group>

          <Form.Group controlId="formJobDescription" className="mt-3">
            <Form.Label>LinkedIN URL:</Form.Label>
            <Form.Control
              type="text"
              className="form"
              value={linkedin}
              onChange={(e) => setLinkedin(e.target.value)}
            />
          </Form.Group>

          <Form.Group controlId="formJobDescription" className="mt-3">
            <Form.Label>Twitter URL:</Form.Label>
            <Form.Control
              type="text"
              className="form"
              value={twitter}
              onChange={(e) => setTwitter(e.target.value)}
            />
          </Form.Group>

          <Button variant="secondary" type="submit" className="mt-3">
            Submit
          </Button>
        </Form>
      </Container>
    </div>
  );
};

export default ProfileForm;
