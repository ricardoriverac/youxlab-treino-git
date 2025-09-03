import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Home from "./pages/Home";
import Produtos from "./pages/Produtos";
import Configuracoes from "./pages/Configuracoes";

// import Navbar from './layout/Navbar'

function App() {
  return (
    <Router>
      {/* <Navbar /> */}
      <Routes>
        <Route exact path="/" element={<Login />}></Route>
        <Route path="/home" element={<Home />}></Route>
        <Route path="/produtos" element={<Produtos />}></Route>
        <Route path="/configuracoes" element={<Configuracoes />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
