import { useState } from 'react';
import './App.css';
import Button from './Button2';

function App() {
    const [contador, setContador] = useState(0);

    function ButtonClicado() {
      alert("Você clicou no Botão!");       //Exibe alerta
      setContador(contador + 1);            // Incrementa o contador
    }
  return (
    <div className="App">
      <h1> Compartilhando dados entre componentes (botoẽs)</h1>
      <Button contador={contador} onClick={ButtonClicado}/>
      <Button contador={contador} onClick={ButtonClicado}/> 
    </div>
  );
}

export default App;
