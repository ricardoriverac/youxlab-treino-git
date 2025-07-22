import Button from './components/Button';
import './App.css';

function App() {
  return (
    <div className="App">

      <h2 style={{color: 'grey'}}>Contadores dos botoẽs se modificam separadamente:</h2>
      < Button />
      < Button />

      <h1>Compartilhando dados entre os componentes (botoẽs)</h1>
    </div>
  );
}

export default App;
