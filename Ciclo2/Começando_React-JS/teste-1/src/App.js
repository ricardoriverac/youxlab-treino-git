import './App.css'; // foi iamportado o arquivo de css da página
import MyButton from './components/MyButton'; // foi importado o arquivo do botão
import MinhaImagem from './assets/imagem.jpg' // foi impotado a imagem 

function App() {
  return (
    <div className="App">
      <h1>Bem vindo ao meu site!</h1>
      <img className='perfil' src={MinhaImagem} />  {/* foi adicionado a imagem no app e foi adicionado uma classe a ela */}
      <MyButton/> {/* foi adicionado o botão no app */}
    </div>
  );
}

export default App; // exporta o App, agora esse arquivo pode ser importado e usado em outros arquivos
