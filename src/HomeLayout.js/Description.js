import React from "react";

const Description = () => {
  const descriptionStyle = {
    fontFamily: "Calibri, sans-serif", // Set Calibri font
  };

  const headingStyle = {
    fontFamily: "Raleway",
    fontSize: "32px", // Set font size for headings
    fontWeight: "bold", // Make the text bold
    color: "#ffcc00", // Darker yellow color
  };

  const paragraphStyle = {
    fontSize: "18px", // Set font size for paragraphs
    marginBottom: "20px", // Add spacing between paragraphs
  };

  return (
    <div className="my-32 ml-10 mr-10 text-black" style={descriptionStyle}>
      <h2 style={headingStyle}>Welcome to BoilerNetwork!</h2>
      <p style={paragraphStyle}>
        This is an innovative platform that automates the often challenging
        process Purdue students face when reaching out to professors for
        research and internship opportunities.
      </p>
      <p style={paragraphStyle}>
        Our application offers a unique gaming experience that allows users to
        navigate through different levels of difficulty while having fun during
        the spooky season.
      </p>
      <p style={paragraphStyle}>
        Whether you're a student looking to make valuable connections or simply
        seeking an entertaining experience, BoilerNetwork has something for
        everyone!
      </p>
    </div>
  );
};

export default Description;
