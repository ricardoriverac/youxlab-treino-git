import './App.css';

const band={  // lista de objetos
    nome: 'Radiohead',
    img: 'https://i.pinimg.com/736x/d9/a2/df/d9a2df2ef681b0537e1213fa4d906ebd.jpg',
    imgTamanho: 300,
}

function App() {
  return (
    <div className="App">
      <h1>{band.nome}</h1>
      <img 
        className="band"
        src={band.img}
        alt={'foto de '+band.nome}
        style={{height: band.imgTamanho, width: band.imgTamanho}}  // aplicamos um css na imagem diretamente 
      />
    </div>
  );  
}

export default App;
