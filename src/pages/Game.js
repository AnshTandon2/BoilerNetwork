import React from "react";

const Game = () => {
  return (
    <div className="flex max-w-none bg-[#3d2c3c] py-10 justify-center">
      <iframe
        src="https://boilernet.streamlit.app/" //add new link
        width="1000"
        height="1000"
        frameborder="no"
        allowfullscreen="true"
        webkitallowfullscreen="true"
        mozallowfullscreen="true"
        scrolling="no"
      ></iframe>
    </div>
  );
};

export default Game;
