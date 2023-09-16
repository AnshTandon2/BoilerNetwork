import React, { useState } from "react";

const Pumpkins = () => {
  // State to hold the user input data
  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();

    // Create a JSON object from the form data
    const userData = {
      username: formData.username,
      password: formData.password,
    };

    // Send the userData to a JSON API endpoint or store it in your desired way
    // For this example, we'll log it to the console
    console.log(userData);

    // Clear the form fields
    setFormData({
      username: "",
      password: "",
    });
  };

  // Function to handle input field changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const containerStyle = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
  };

  const formStyle = {
    width: "300px",
    textAlign: "center",
    fontFamily: "Calibri, sans-serif",
  };

  const buttonStyle = {
    backgroundColor: "#F5DEB3", // Light tan color
    color: "black",
  };

  return (
    <div style={containerStyle}>
      <form style={formStyle} onSubmit={handleSubmit}>
        <h1 className="text-white text-7xl mb-6">Sign In</h1>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          className="rounded-md px-4 py-2 mb-2 text-black w-full"
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          className="rounded-md px-4 py-2 mb-4 text-black w-full"
        />
        <button
          type="submit"
          style={buttonStyle}
          className="rounded-md px-4 py-2 w-full"
        >
          Sign In
        </button>
      </form>
    </div>
  );
};

export default Pumpkins;
