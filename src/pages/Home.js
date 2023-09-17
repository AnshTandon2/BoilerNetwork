import React from "react";
import AboutUs from "../HomeLayout.js/AboutUs";
import Description from "../HomeLayout.js/Description";
import GameGallery from "../HomeLayout.js/GameGallery";

import { NavLink } from "../NavbarElements";
import { Form } from "react-router-dom";

const Home = () => {
  // Light tan color
  const lightTan = "#F5DEB3";

  return (
    <>
      <div
        className="flex max-w-none py-10"
        style={{
          background: lightTan,
        }}
      >
        <Description />
        <GameGallery />
      </div>
      <div
        className="bg-[#FFD700] py-10 justify-center"
        style={{
          background: lightTan, // Use the same lightTan color here
        }}
      >
        {/* <form>
          <label>
            Name:
            <input type="text" name="name" />
          </label>
          <label>
            Password:
            <input type="text" name="password" />
          </label>
          <input type="submit" value="submit" />
          <button>Submit</button>
        </form> */}
        <NavLink
          to="/game"
          activeStyle={{ color: "black" }}
          className="navbutton justify-center"
        >
          <a
            href="https://boilernet.streamlit.app/"
            className="p-5 px-10 rounded-full bg-[#ffc77d] text-[#f5764f] font-semibold text-xl hover:bg-[#fcb04c] hover:text-[#fa6d42]"
          >
            Continue
          </a>
        </NavLink>
      </div>

      <div
        className="flex max-w-none py-10"
        style={{
          background: lightTan,
        }}
      >
        <AboutUs />
      </div>
    </>
  );
};

export default Home;
