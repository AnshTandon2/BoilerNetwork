import React from "react";
import { useState } from "react";

// component
import Creators from "./Creators";

const AboutUs = () => {
  let Image1 = require("../assets/anshpho.jpeg");
  let Image2 = require("../assets/shrung.jpeg");
  let Image3 = require("../assets/arnav.jpeg");
  let Image4 = require("../assets/steven.jpg");

  const [names, setNames] = useState([
    {
      image: Image1,
      name: "Ansh",
    },
    {
      image: Image2,
      name: "Shrung",
    },
    {
      image: Image3,
      name: "Arnav",
    },
    {
      image: Image4,
      name: "Steven",
    },
  ]);

  return (
    <div>
      <div>
        <h1 className="text-center text-6xl font-extrabold text-[#ffc77d] ">
          About Us
        </h1>
      </div>
      <div className="grid grid-cols-4 gap-10 mx-10 mt-10 ">
        {names.map((user, index) => {
          return <Creators key={index} name={user.name} image={user.image} />;
        })}
      </div>
    </div>
  );
};

export default AboutUs;
