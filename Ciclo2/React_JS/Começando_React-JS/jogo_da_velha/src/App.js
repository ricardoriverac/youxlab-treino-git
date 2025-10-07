import { useState } from 'react';
import ReiniciarJogo from './components/ReiniciarJogo';
import Tabuleiro from './components/Tabuleiro';
import CalculaVencedor from './components/CalculandoVencedor';
import './App.css';


function App() {
  const [quadrados, setQuadrados]=useState(Array(9).fill(null))
  const [vezDeX, setVezDeX]=useState(true)

  const ganhador= CalculaVencedor(quadrados)

  function IndentificaClicado(index){
    if(quadrados[index] || ganhador){
      return
    }
    const proximoQuadrado=[...quadrados]
    proximoQuadrado[index]= vezDeX ? 'X':'O'
    setQuadrados(proximoQuadrado)
    setVezDeX(!vezDeX)
  }

  const status= ganhador ? `Ganhador: ${ganhador}` : `Próximo Jogador: ${vezDeX ? 'X': 'O'}`


  return (
    <div className="App">
      <h1>Jogo da Velha</h1>
      <p>{status}</p>
      <Tabuleiro quadrados={quadrados} onClick={IndentificaClicado} />
      <ReiniciarJogo/>
    </div>
  );
}

export default App;
