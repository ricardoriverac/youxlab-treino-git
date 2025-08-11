import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./components/pages/Home";
import Contato from "./components/pages/Contato";
import Empresa from "./components/pages/Empresa";
import NavBar from "./components/layout/NavBar";
import Footer from "./components/layout/footer";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route exact path="/" element={<Home />}></Route>
        <Route exact path="/empresa" element={<Empresa />}></Route>
        <Route exact path="/contato" element={<Contato />}></Route>
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
