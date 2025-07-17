import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Empresa from "./components/Empresa";
import Contato from "./components/Contato";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Empresa" element={<Empresa />} />
        <Route path="/Contato" element={<Contato />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
