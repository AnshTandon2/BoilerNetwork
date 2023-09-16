import React from 'react'

const Creators = (props) => {
  return (
    <div className='-my-0 py-10 '>
    {/* Image */}
    
    <div className='p-10 bg-[#ffe4d1] rounded-2xl'>
        <img src={props.image} />
        <h1 className='text-[#ff7d7d] text-center font-medium mt-3 text-3xl'>{props.name}</h1>
        
    </div>

    </div>
  )
}

export default Creators