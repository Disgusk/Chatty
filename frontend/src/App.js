import './App.css';
import { Div, Button, Icon, Input } from "atomize";
import { useState } from 'react';
import AudioReactRecorder, { RecordState } from 'audio-react-recorder'
 


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
  const [pronuns, setPronuns] = useState({hello: "90", bye: "80", good: "70", bad: "60",  how: "50", are: "40", you: "30", today: "20", fine: "10"});
  
  // initialize recording stuff
  const [recordState, setRecord] = useState(null);

  const start = () => {
    setRecord(RecordState.START)
  }
 
  const stop = () => {
    setRecord(RecordState.STOP)
  }
 
  //audioData contains blob and blobUrl
  const onStop = (audioData) => {
    console.log('audioData', audioData)
  }


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


  const getColor = (value) => {
    // get int value from string percentage
    
    //value = value.replace("%", "")
   
    if (value > 80) {
      return "#2cba00"
    } else if (value > 60) {
      return "#a3ff00"
    } else if (value > 40) {
      return "#fff400"
    } else if (value > 20) {
      return "#ffa700"
    } else {
      return "#ff0000"
    }
  }

  async function addAudioElement (blob) {  
    console.log(blob['blob'])  
    var file = new File([blob['blob']], "userAudio.wav");
    const data = new FormData();
    data.append('file', file);
    
    // audio works file
    // const audio = document.createElement("audio");
    // audio.src = blob['url'];
    // audio.controls = true;
    // document.body.appendChild(audio);

    let response = await fetch('http://localhost:5000/getResponse?audioUrl='+blob['url'], {method: 'POST', body:data}).then(
      console.log(response) 
    )
   
    // URL.revokeObjectURL(blob)
  };

  return (
    // main div that will have the whole page
    <Div
      d="flex"
      flexDir="column"    
      w="100%"
      h="90vh"
      textColor="black"
    >
      
      <Div
        d="flex"
        flexDir="row"
        align="flex-start"
        // bg="#362eaa"
        w="100%"
        h="90vh"        
        textColor="black"
        // div that will have both chat and pronunciation
      
      >

        <Div
          d="flex"
          align="flex-start"
          bg="#7df8fe35"
          w="100%"
          h="100%"        
          textColor="black"
          // chat window Div

        >

          <Div
            d="flex"            
            flexDir="column"                                                    
            overflowY="scroll"
            m={{ t: "1rem" , r: "2rem", l: "2rem"}}
            >

            <Div
              bg="#21677eff"
              shadow="3"
              textColor="white"
              d="flex"
              align="flex-start"
              w="100%"
              display="flex"                
              m={{ t: "1rem" , r: "2rem"}}
              h="auto"
              p={{ l: "2%", b: "2%", t: "2%" }}
              rounded="md"              
              >
              "What are your symptoms?"
            </Div>

            <Div  
              bg="#00d640ff"              
              shadow="3"
              textColor="white"
              d="flex"
              align="flex-end"
              w="100%"
              display="flex"
              m={{ t: "1rem" , r:"2rem"}}
              h="auto"
              p={{ l: "2%", b: "2%", t: "2%" , r: "2%"}}
              rounded="md"                
              >              
              Nothing, I'm fine.

            </Div>                 
                                                                                          
          </Div>

        </Div>

        <Div          
          d="flex"          
          w="100%"          
          maxW= "100%"
          maxH="100%"        
          textColor="black"
          overflow="scroll"
          flexWrap = "wrap"
          // pronunciation window div

        >
                    
          {Object.entries(pronuns).map(([key,value]) => (
              <Div
                bg={getColor(value)}
                h = "auto"
                shadow="3"
                rounded="md"
                textColor="white"
                p = {{ l: "2%", b: "2%", t: "2%" , r: "2%"}}
                m = {{ t: "1rem" , l: "0.5rem", r: "0.5rem"}}
                key={key}
              >
                {key} 
              </Div>
                                        
            ))}
            

        </Div>

      </Div>

            
      <AudioReactRecorder state={recordState} onStop={addAudioElement} canvasHeight={50} />

      <Div
        d="flex"
        align="flex-end"
        justify="center"        
        w="100%"
        h="10vh"        
        textColor="black"
        // this div will have mic button
      >        

        

        <Button
          h="2.5rem"
          w="2.5rem"
          bg="success700"
          hoverBg="success600"
          rounded="circle"
          m={{ r: "1rem" }}
          onClick={start}
          shadow="2"
          hoverShadow="4"
        >
          
          <Icon name="Play" size="20px" color="white" />
        </Button>

        <Button
          h="2.5rem"
          w="2.5rem"
          bg="success700"
          hoverBg="success600"
          rounded="circle"
          m={{ r: "1rem" }}
          shadow="2"
          hoverShadow="4"
          onClick={stop}
        >
          <Icon name="Stop" size="20px" color="white" />   
        </Button>

      </Div>

    </Div>
  );
}


export default App;
