import React , {useEffect,useState} from 'react'

function App () {

  const [backEndData, SetBackEnddata]= useState([{}])
  useEffect( ()=>{

    fetch("/api").then(
      response=> response.json()
    ).then(
      
      data=> {
        SetBackEnddata(data)
      }
    )


  }, []
  ) 
  
  

  return (
    <div>

      backEndData

    </div>
  )
}

export default App