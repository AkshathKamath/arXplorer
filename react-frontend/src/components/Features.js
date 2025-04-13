import React from "react";
import "../styles/Features.css";

const FeaturesComponent = () => {
  return (
    <div>
      <h5>Features</h5>
      <table className="table table-hover table-bordered">
        <tbody>
          <tr>
            <td className="features">
              <th>Summarize your resume in seconds.</th>
              Generate a brief, two-line summary of your resume, highlighting
              yourmost relevant skills and experiences. This feature provides a
              quick snapshot for easy review. Use it directly as your LinkedIN
              bio!
            </td>
          </tr>
          <tr>
            <td className="features">
              <th>Create the Ideal resume for your dream role.</th>
              Compare how well your resume fits with the Job description of your
              dream role. Generate a score that rates the resume-JD fit and also
              suggests improvements you can make that increases your chances of
              getting shortlisted!
            </td>
          </tr>
          <tr>
            <th className="features">More features coming soon!</th>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default FeaturesComponent;
