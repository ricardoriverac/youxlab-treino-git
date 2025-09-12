import { Link } from "react-router-dom";

import styles from "./Navbar.module.css";
import logo from "../../img/costs_logo.png";
import Container from "./Container";

function Navbar() {
  return (
    <nav class={styles.navbar}>
      <Container>
        <Link to="/">
          <img src={logo} alt="Costs" />
        </Link>
        <ul className={styles.list}>
          <li className={styles.links}>
            <Link to="/" class={styles.link1}>Home</Link>
          </li>
          <li className={styles.links}>
            <Link to="/projects" class={styles.link1}>Projetos</Link>
          </li>
          <li class={styles.links}>
            <Link to="/empresa" class={styles.link1}>Empresa</Link>
          </li>
          <li class={styles.links}>
            <Link to="/contato" class={styles.link1}>Contato</Link>
          </li>
        </ul>
      </Container>
    </nav>
  );
}

export default Navbar;
