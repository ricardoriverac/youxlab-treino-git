import { Link } from "react-router-dom"
import styles from './NavBar.module.css'


function NavBar(){
    return (
      
       <ul className={styles.list}>
        <li className={styles.iten}>
           <Link to="/">home</Link>
        </li>
        <li className={styles.iten}>
          <Link to="/empresa">Empresa</Link>
        </li>
        <li className={styles.iten}>
          <Link to="/contato">Contato</Link>
        </li>
       </ul>
    )
}

export default NavBar