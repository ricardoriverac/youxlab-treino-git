import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

//Pages
import Inicio from "./Componentes/Paginas/Inicio";
import Company from "./Componentes/Paginas/Company";
import NovoProjeto from "./Componentes/Paginas/NovoProjeto";
import Contact from "./Componentes/Paginas/Contact";

//Layout
import Container from "./Componentes/Layout/Container";
import NavBar from "./Componentes/Layout/NavBar";
import Footer from "./Componentes/Layout/Footer";

function App() {
  return (
      <Router>
        <NavBar />
        <Container customClass="min-height">
          <Routes>
            <Route exect path="/" element={<Inicio />}></Route>
            <Route path="/contact" element={<Contact />}></Route>
            <Route path="/company" element={<Company />}></Route>
            <Route path="/novoprojeto" element={<NovoProjeto />}></Route>
          </Routes>
        </Container>
        <Footer />
      </Router>
  );
}

export default App;
