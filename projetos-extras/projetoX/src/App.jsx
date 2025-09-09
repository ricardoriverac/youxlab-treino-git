import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Home from "./pages/Home";
import Produtos from "./pages/Produtos";
import Configuracoes from "./pages/Configuracoes";
import Navbar from "./layout/Navbar";
import Container from "./layout/Container";

function App() {
  return (
    <Router>
      {/* <Container customClass='min-height'> */}
        <Routes>
          <Route exact path="/" element={<Login />}></Route>
          <Route path="/home" element={<Navbar> <Home /> </Navbar>}></Route>
          <Route path="/produtos" element={<Navbar> <Produtos /> </Navbar>}></Route>
          <Route path="/Configurações" element={<Navbar> <Configuracoes /></Navbar>}></Route>
        </Routes>
      {/* </Container> */}
    </Router>
  );
}

export default App;
