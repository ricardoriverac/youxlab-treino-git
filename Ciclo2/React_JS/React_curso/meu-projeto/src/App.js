import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Empresa from "./pages/Empresa";
import Contato from "./pages/Contato";
import Navbar from "./Components/layouts/Navbar";
import Footer from "./Components/layouts/Footer";

function App() {
  return (
    <Router>

      <Navbar/>

      <Routes>                                    {/* Declara URLs e o que estão se referindo */}
        <Route exact path="/" element ={<Home/>}/>
        <Route path="/empresa" element ={<Empresa/>}/>
        <Route path="/contato" element ={<Contato/>}/>              {/* Declara o caminho da função tal */}
      </Routes>
      <Footer/>

    </Router>

  );
}

export default App;
