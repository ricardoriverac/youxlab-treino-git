import { useState } from "react";
import "./App.css";
import Saudacao from "./Components/Saudacao";
import SeuNome from "./Components/SeuNome";

function App() {
  const [nome, setNome] = useState();
  return (
    <>
      <div className="App">
        <h1>State lift</h1>
        <SeuNome setNome={setNome}/>
        <Saudacao nome={nome} />
      </div>
    </>
  );
}

export default App;
