import { Link } from "react-router-dom";
import Container from "./Container";
// import styles from "./NavBar.module.css";
import costs_logo from './costs_logo.png'

function NavBar() {

  return (
    <nav>
      <Container>
        <Link to = "/">
        <img src= {costs_logo} alt="Costs" />
        </Link>
        <Link to="/">Home</Link>
        <Link to="/contact">Contato</Link>
        <Link to="/company">Empresa</Link>
        <Link to="/newproject">Novo projeto</Link>
      </Container>
    </nav>
  );
}
export default NavBar;
