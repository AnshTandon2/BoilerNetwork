import React from 'react'

const GameGallery = () => {
    function goRight() {
        document.querySelector(".allPages").scrollLeft += 240;
    }
    
    function goLeft() {
        document.querySelector(".allPages").scrollLeft -= 240;
    }

    let Image1 = require('../assets/purdue.png');
    
  return (
    
    <div className='flex justify-end'>
        <div className=''>
        <img src={Image1} alt="link" className='w-100 h-auto  mt-10' />
        <div className="Left">
            <button className=" bg-slate-600 w-1" onclick="goLeft()">
                
            </button>
            <div className="allPages mx-48 ">

                
                    
                    
                    
                

                
                {/* <div className="allpage"id="page2">
                    <h1 className=" p-40 bg-slate-300 w-60 ml-4">
                        World
                    </h1>
                </div> */}
            </div>
        </div>
        </div>
    </div>
  )
}

export default GameGallery