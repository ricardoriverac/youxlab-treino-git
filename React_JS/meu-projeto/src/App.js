import "./App.css";
import Evento from "./Components/Evento";
import Form from "./Components/Form";

function App() {

  return (
    <div className="App">
      <h1>Testando Eventos</h1>
      <Evento numero="1"/>
      <Evento numero="2"/>
      <Form/> 
    </div>
  );
}

export default App;
