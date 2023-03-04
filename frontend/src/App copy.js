import './App.css';
import { Div, Button, Icon, Input } from "atomize";
import { useState } from 'react';

/*
    display: flex;
    position: absolute;
    flex-direction: column;
    width: 100%;
    height: 90%;
    justify-content: flex-end;
*/

function App() {

  const [botmessages, setBotMessages] = useState([]);
  const [usermessages, setUserMessages] = useState([]);


  const [currentMessage, setCurrentMessage] = useState("");

  async function getResponse () {

    const params = {
      'userInput' : currentMessage
    };

    const options = {
      method: 'POST',
      body: JSON.stringify( params )
    };

    console.log(params)

    let value = await fetch('http://127.0.0.1:5000/response?userInput='+currentMessage).then(response => response.json());
    //.then(data => this.setState({ totalReactPackages: data.total }));


    setBotMessages([...botmessages, value['response']])
    setUserMessages([...usermessages, currentMessage])
    
    
  }

  const handleChange = (e) => {
    setCurrentMessage(e.target.value)
  }


  return (
    <Div
      display="flex"
      flexDir="row"
      h="100%"
      >
        

        <Div
          d="flex"
          pos="absolute"
          flexDir="column"
          overflow = "scroll"
          w="50%"
          h="90%"          
          justify="flex-end"          
          overflowY="scroll"
          >

          <Div
            bg="#57caa26b"
            d="flex"
            align="left"
            w="50%"
            display="flex"                
            m={{ t: "1rem" }}
            h="auto"
            p={{ l: "2%", b: "2%", t: "2%" }}
            rounded="md"
            >
          "What are your symptoms?"
          </Div>

          <Div  
            bg="#7b45a76b"
            d="flex"
            align="right"
            w="50%"
            display="flex"
            m={{ t: "1rem" , r:"2rem"}}
            h="auto"
            p={{ l: "2%", b: "2%", t: "2%" , r: "2%"}}
            rounded="md"                
            >
            "Nothing, I'm fine."

          </Div>                 
                                                                                        
        </Div>

        <Div
          d="flex"
          pos="absolute"
          flexDir="column"
          overflow = "scroll"
          w="50%"
          h="90%"          
          //justify="flex-end"          
          overflowY="scroll"
          >

          <Div
            bg="#57caa26b"
            d="flex"
            align="left"
            w="50%"
            display="flex"                
            m={{ t: "1rem" }}
            h="auto"
            p={{ l: "2%", b: "2%", t: "2%" }}
            rounded="md"
            >
          "What are your symptoms?"
          </Div>

          <Div  
            bg="#7b45a76b"
            d="flex"
            align="right"
            w="50%"
            display="flex"
            m={{ t: "1rem" , r:"2rem"}}
            h="auto"
            p={{ l: "2%", b: "2%", t: "2%" , r: "2%"}}
            rounded="md"                
            >
            "Nothing, I'm fine."

          </Div>                 
                                                                                        
        </Div>
              
  
    </Div>
  );
}


export default App;
