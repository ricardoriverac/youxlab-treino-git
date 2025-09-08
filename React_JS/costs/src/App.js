import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./components/pages/Home";
import Company from "./components/pages/Company";
import Contact from "./components/pages/Contact";
import NewProject from "./components/pages/NewProject";

import Container from "./components/layout/Container";

function App() {
  return (
    <Router>
      <div className="App">
        <ul>
          <Link to="/">Home</Link>
          <Link to="/company">Company</Link>
          <Link to="/contact">Contact</Link>
          <Link to="/newproject">New Project</Link>
        </ul>
        <Container customClass="min-height">
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/company" element={<Company />} />
            <Route exact path="/contact" element={<Contact />} />
            <Route exact path="/newproject" element={<NewProject />} />
          </Routes>
        </Container>
        <p>footer</p>
      </div>  
    </Router>
  );
}

export default App;
